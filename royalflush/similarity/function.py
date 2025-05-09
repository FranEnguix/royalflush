from abc import ABCMeta, abstractmethod
from typing import Dict

import torch
from torch import Tensor

from .similarity_vector import SimilarityVector


class SimilarityFunction(object, metaclass=ABCMeta):

    @abstractmethod
    def get_similarity_vector(
        self,
        layers1: Dict[str, Tensor],
        layers2: Dict[str, Tensor],
    ) -> SimilarityVector:
        raise NotImplementedError


class OnesFunction(SimilarityFunction):

    def get_similarity_vector(
        self,
        layers1: Dict[str, Tensor],
        layers2: Dict[str, Tensor],
    ) -> SimilarityVector:
        vector: Dict[str, float] = Dict()
        for layer in layers1:
            if not layer in layers2:
                raise ValueError(f"Layer {layer} not present in {list(layers2.keys())}.")
            vector[layer] = 1
        return SimilarityVector(vector=vector)


class EuclideanDistanceFunction(SimilarityFunction):

    def get_similarity_vector(
        self,
        layers1: Dict[str, Tensor],
        layers2: Dict[str, Tensor],
    ) -> SimilarityVector:
        vector: Dict[str, float] = Dict()

        for layer in layers1:
            if not layer in layers2:
                raise ValueError(f"Layer {layer} not present in {list(layers2.keys())}.")

            diff = layers1[layer] - layers2[layer]
            euclidean_distance = torch.norm(diff).item()

            vector[layer] = euclidean_distance

        return SimilarityVector(vector=vector)
