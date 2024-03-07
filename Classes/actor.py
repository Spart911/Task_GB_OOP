
from abc import ABC
from Interfaces.i_actor_behaviour import iActorBehaviour

class Actor(iActorBehaviour):

    name: str
    isTakeOrder: bool = False
    isMakeOrder: bool = False
    isReturnRequested: bool = False
    def __init__(self, name: str):
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self) -> str:
        return self.name
    
    def setTakeOrder(self, value: bool):
        self.isTakeOrder = value

    def getTakeOrder(self) -> bool:
        return self.isTakeOrder
    
    def setMakeOrder(self, value: bool):
        self.isMakeOrder = value

    def getMakeOrder(self) -> bool:
        return self.isMakeOrder

    def requestReturn(self):
        self.isReturnRequested = True
        print(f"{self.name} has requested a return.")

    def processReturn(self):
        if self.isReturnRequested:
            print(f"{self.name} is processing the return.")
        else:
            print(f"{self.name} has no return request.")

    def confirmReturn(self):
        if self.isReturnRequested:
            print(f"{self.name} confirms the return.")
            self.isReturnRequested = False
        else:
            print(f"{self.name} has no return request to confirm.")


