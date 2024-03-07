from abc import ABC, abstractmethod

class iReturnOrder(ABC):
    @abstractmethod
    def requestReturn(self):
        pass

    @abstractmethod
    def processReturn(self):
        pass

    @abstractmethod
    def confirmReturn(self):
        pass

    @abstractmethod
    def getActor(self) -> str:
        pass