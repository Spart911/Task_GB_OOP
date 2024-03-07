from typing import List
from Classes.actor import Actor
from Classes.promotional_client import PromotionalClient
from Interfaces.i_actor_behaviour import iActorBehaviour
from Interfaces.i_market_behaviour import iMarketBehaviour
from Interfaces.i_queue_behaviour import iQueueBehaviour
from Interfaces.i_return_order import iReturnOrder


class Market(iMarketBehaviour, iQueueBehaviour):
    def __init__(self):
         self.queue : List[iActorBehaviour] = []


    def acceptToMarket(self, actor: iActorBehaviour):
        print(actor.getActor() + " клиент пришел в магазин ")
        self.takeInQueue(actor)

    def takeInQueue(self, actor: iActorBehaviour):
        self.queue.append(actor)
        print(actor.getActor() + " клиент добавлен в очередь ")

    def releaseFromMarket(self, actors: List[Actor]):
        for actor in actors:
            print(actor + " клиент ушел из магазина ")
            # self.queue.remove(actor)

    def update(self):
        self.takeOrder()
        self.process_return()
        self.giveOrder()
        self.releaseFromQueue()


    def giveOrder(self):
        for actor in self.queue:
            if isinstance(actor, PromotionalClient):
                actor.processReturn()
            elif actor.isMakeOrder:
                actor.setTakeOrder(True)
                print(actor.getActor() + " клиент получил свой заказ ")

    def releaseFromQueue(self):
        releaseActors: List[str] = []
        for actor in self.queue:
            if isinstance(actor, PromotionalClient):
                actor.confirmReturn()
            if actor.isTakeOrder:
                releaseActors.append(actor.getActor())
                print(actor.getActor() + " клиент ушел из очереди ")
        self.releaseFromMarket(releaseActors)

    def takeOrder(self):
        for actor in self.queue:
            if not actor.isMakeOrder:
                actor.setMakeOrder(True)
                print(actor.getActor() + " клиент сделал заказ ")
    def process_return(self):
        for actor in self.queue:
            if isinstance(actor, PromotionalClient):
                actor.requestReturn()



    def process_return_promotional_client(self, actor: iReturnOrder):
        # Реализация обработки возврата товара для PromotionalClient
        print(f"Обработка возврата для акционного клиента {actor.get_actor()}")
        # Дополнительная логика обработки возврата

    def confirm_return_promotional_client(self, actor: iReturnOrder):
        # Реализация подтверждения возврата для PromotionalClient
        print(f"Возврат подтвержден для акционного клиента {actor.get_actor()}")