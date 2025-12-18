from abc import ABC, abstractmethod

class Algoritmo(ABC):

    @abstractmethod
    def executa_algoritmo(self, cadeia_ref: list[int], total_quadros: int) -> dict:
        pass