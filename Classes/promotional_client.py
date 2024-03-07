from Classes.actor import Actor


class PromotionalClient(Actor):
    # Статическое поле, представляющее количество участников в акции
    promotional_clients_count = 0

    def __init__(self, name: str, action_name: str, id: int, max_participants: int):
        super().__init__(name)
        self.idVIP = id
        self.action_name = action_name
        self.max_participants = max_participants
        self.participants_count = 0

        # Увеличиваем количество акционных клиентов при создании нового объекта
        PromotionalClient.promotional_clients_count += 1

    def getActionName(self):
        return self.action_name

    def getActor(self):
        return self.getName()

    def getName(self):
        return super().getName()

    def getClientId(self):
        return self.client_id

    def setClientId(self, client_id):
        self.client_id = client_id

    @staticmethod
    def getPromotionalClientsCount():
        return PromotionalClient.promotional_clients_count

    def requestReturn(self):
        # Реализация запроса возврата
        if self.participants_count > self.max_participants:
            print(
                 f"Клиент {self.getName()} отказано в обслуживании из-за превышения максимального числа участников в акции.")
            return False
        return True

    def processReturn(self):
        # Реализация обработки возврата товара
        print(f"Обработка возврата для клиента {self.getName()}")
        # Дополнительная логика обработки возврата

    def confirmReturn(self):
        # Реализация подтверждения возврата
        print(f"Возврат подтвержден для клиента {self.getName()}")


    def setName(self, name):
        super().name = name

    def isTakeOrder(self):
        return super().getTakeOrder()

    def setTakeOrder(self, takenOrder):
        super().setTakeOrder(takenOrder)

    def isMakeOrder(self):
        return super().getMakeOrder()

    def setMakeOrder(self, makeOrder):
        super().setMakeOrder(makeOrder)
