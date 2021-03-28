"""Service class"""

from abc import ABC, abstractmethod


class Service(ABC):
    """Service class"""

    @abstractmethod
    def start(self):
        """Starts service"""

    @abstractmethod
    def shutdown(self):
        """Shuts service down"""
