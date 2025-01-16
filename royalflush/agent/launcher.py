from aioxmpp import JID

from .base import AgentBase
from .premiofl.base import PremioFlAgent


class LauncherAgent(AgentBase):
    """
    LauncherAgent is responsible for:
    1) Setting up presence handlers.
    2) Launching actual FL agents based on the Experiment & Graph.
    """

    def __init__(
        self,
        jid: str,
        password: str,
        agents: list[PremioFlAgent],
        max_message_size: int,
        agents_coordinator: JID,
        agents_observers: list[JID],
        web_address: str = "0.0.0.0",
        web_port: int = 10000,
        verify_security: bool = False,
    ):
        self.agents = agents
        self.agents_coordinator = agents_coordinator
        self.agents_observers = [] if agents_observers is None else agents_observers
        super().__init__(jid, password, max_message_size, web_address, web_port, verify_security)
        self.logger.debug(f"Agents to launch: {[a.jid.bare() for a in self.agents]}")

    async def setup(self) -> None:
        from ..behaviour.launcher import LaunchAgentsBehaviour, Wait

        self.setup_presence_handlers()
        self.presence.set_available()
        self.add_behaviour(LaunchAgentsBehaviour())
        self.add_behaviour(Wait())

    async def launch_agents(self) -> None:
        """
        Creates and starts the actual FL agents based on the Experiment settings
        and the .gml graph structure.
        """
        self.logger.debug(f"Initializating launch of {[str(a.jid.bare()) for a in self.agents]}")
        for agent in self.agents:
            neighbour_jids = agent.neighbours
            self.logger.debug(
                f"The neighbour JIDs for agent {agent.jid.bare()} are {[str(j.bare()) for j in neighbour_jids]}"
            )

        for agent in self.agents:
            await agent.start()
