from abc import abstractmethod

class BaseSerializer():
    @abstractmethod
    def serialize(self, data):
        return

    @abstractmethod
    def deserialize(self, data):
        return
