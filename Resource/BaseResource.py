from abc import ABC, abstractmethod


class BaseResource(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def to_dict(self):
        pass
