from abc import ABCMeta, abstractmethod
from queue import Queue
from typing import OrderedDict

from aioxmpp import JID
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
from torch import Tensor

from royalflush.behaviour.premiofl.fsm import PremioFsmBehaviour
from royalflush.behaviour.premiofl.layer_receiver import LayerReceiverBehaviour
from royalflush.behaviour.premiofl.similarity_receiver import SimilarityReceiverBehaviour
from royalflush.datatypes.consensus import Consensus
from royalflush.datatypes.consensus_manager import ConsensusManager
from royalflush.datatypes.models import ModelManager
from royalflush.log.algorithm import AlgorithmLogManager
from royalflush.log.message import MessageLogManager
from royalflush.log.nn import NnConvergenceLogManager, NnInferenceLogManager, NnTrainLogManager
from royalflush.similarity.similarity_manager import SimilarityManager
from royalflush.similarity.similarity_vector import SimilarityVector

from ..base import AgentNodeBase


class PremioFlAgent(AgentNodeBase, metaclass=ABCMeta):

    def __init__(
        self,
        jid: str,
        password: str,
        max_message_size: int,
        consensus_manager: ConsensusManager,
        model_manager: ModelManager,
        similarity_manager: SimilarityManager,
        observers: list[JID] | None = None,
        neighbours: list[JID] | None = None,
        coordinator: JID | None = None,
        max_rounds: None | int = 100,
        web_address: str = "0.0.0.0",
        web_port: int = 10000,
        verify_security: bool = False,
    ):
        extra_name = f"agent.{JID.fromstr(jid).localpart}"
        self.consensus_manager = consensus_manager
        self.model_manager = model_manager
        self.similarity_manager = similarity_manager
        self.max_rounds = max_rounds  # None = inf
        self.current_round: int = 0
        self.consensus_transmissions: Queue[Consensus] = Queue()
        self.message_logger = MessageLogManager(extra_logger_name=extra_name)
        self.algorithm_logger = AlgorithmLogManager(extra_logger_name=extra_name)
        self.nn_train_logger = NnTrainLogManager(extra_logger_name=extra_name)
        self.nn_inference_logger = NnInferenceLogManager(extra_logger_name=extra_name)
        self.nn_convergence_logger = NnConvergenceLogManager(extra_logger_name=extra_name)

        self.fsm_behaviour = PremioFsmBehaviour()
        self.layer_receiver_behaviour = LayerReceiverBehaviour()
        self.similarity_receiver_behaviour = SimilarityReceiverBehaviour()
        post_coordination_behaviours = [
            (self.fsm_behaviour, None),
            (
                self.layer_receiver_behaviour,
                Template(metadata={"rf.conversation": "layers"}),
            ),
            (
                self.similarity_receiver_behaviour,
                Template(metadata={"rf.conversation": "similarity"}),
            ),
        ]

        super().__init__(
            jid,
            password,
            max_message_size,
            observers,
            neighbours,
            coordinator,
            post_coordination_behaviours,
            web_address,
            web_port,
            verify_security,
        )

    def select_neighbours(self) -> list[JID]:
        """
        Get the selected available neighbours to share the model layers, based on the implementation criteria.

        Raises:
            NotImplementedError: _select_neighbours must be overrided or it raises this error.

        Returns:
            list[JID]: The list of the selected available neighbours.
        """
        return self._select_neighbours(self.get_available_neighbours())

    @abstractmethod
    def _select_neighbours(self, neighbours: list[JID]) -> list[JID]:
        raise NotImplementedError

    @abstractmethod
    def _assign_layers(
        self,
        my_vector: None | SimilarityVector,
        neighbours_vectors: dict[JID, SimilarityVector],
        selected_neighbours: list[JID],
    ) -> dict[JID, OrderedDict[str, Tensor]]:
        """
        Assigns which layers will be sent to each neighbour. In the paper this function is coined as `S_L_N`.

        Args:
            my_vector (SimilarityVector): The neighbours that will receive the layers of the neural network model.
            neighbours_vectors (dict[JID, SimilarityVector]): All neighbours' vectors, here are selected and non-selected neighbours.
            selected_neighbours (list[JID]): The neighbours that will receive the layers of the neural network model.

        Raises:
            NotImplementedError: This function must be overrided or it raises this error.

        Returns:
            dict[JID, OrderedDict[str, Tensor]]: The keys are the neighbour's `aioxmpp.JID`s and the values are the
            layer names with the `torch.Tensor` weights or biases.
        """
        raise NotImplementedError

    def assign_layers(
        self,
        selected_neighbours: list[JID],
    ) -> dict[JID, OrderedDict[str, Tensor]]:
        """
        Assigns which layers will be sent to each neighbour. In the paper this function is coined as `S_L_N`.

        Args:
            selected_neighbours (list[JID]): The neighbours that will receive the layers of the neural network model.

        Raises:
            NotImplementedError: This function must be overrided or it raises this error.

        Returns:
            dict[JID, OrderedDict[str, Tensor]]: The keys are the neighbour's `aioxmpp.JID`s and the values are the
            layer names with the `torch.Tensor` weights or biases.
        """
        return self._assign_layers(
            my_vector=self.similarity_manager.get_own_similarity_vector(),
            neighbours_vectors=self.similarity_manager.similarity_vectors,
            selected_neighbours=selected_neighbours,
        )

    async def send_similarity_vector(
        self,
        neighbour: JID,
        vector: SimilarityVector,
        thread: None | str = None,
        metadata: None | dict[str, str] = None,
        behaviour: None | CyclicBehaviour = None,
    ) -> None:
        msg = vector.to_message()
        msg.sender = str(self.jid.bare())
        msg.to = str(neighbour.bare())
        msg.thread = thread
        msg.metadata = metadata
        tag = "-REQREPLY" if vector.request_reply else ""
        await self.__send_message(message=msg, behaviour=behaviour, log_tag=f"-SIMILARITY{tag}")

    async def send_local_layers(
        self,
        neighbour: JID,
        request_reply: bool,
        layers: OrderedDict[str, Tensor],
        thread: None | str = None,
        metadata: None | dict[str, str] = None,
        behaviour: None | CyclicBehaviour = None,
    ) -> None:
        ct = Consensus(layers=layers, sender=self.jid, request_reply=request_reply)
        msg = ct.to_message()
        msg.sender = str(self.jid.bare())
        msg.to = str(neighbour.bare())
        msg.thread = thread
        msg.metadata = metadata
        tag = "-REQREPLY" if request_reply else ""
        await self.__send_message(message=msg, behaviour=behaviour, log_tag=f"-LAYERS{tag}")

    async def __send_message(self, message: Message, behaviour: CyclicBehaviour, log_tag: str = "") -> None:
        await self.send(message=message, behaviour=behaviour)
        self.message_logger.log(
            current_round=self.current_round,
            sender=message.sender,
            to=message.to,
            msg_type=f"SEND{log_tag}",
            size=len(message.body),
            thread=message.thread,
        )

    def are_max_iterations_reached(self) -> bool:
        return self.max_rounds is not None and self.current_round > self.max_rounds

    async def stop(self) -> None:
        await super().stop()
        self.logger.info("Agent stopped.")
