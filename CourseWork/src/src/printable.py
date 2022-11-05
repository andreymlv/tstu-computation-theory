from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self) -> str:
        """
        Create printable string for CLI.
        """
        pass
