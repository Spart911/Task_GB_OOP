from Classes.market import Market
from Classes.ordinary_client import OrdinaryClient
from Classes.promotional_client import PromotionalClient
from Classes.special_client import SpecialClient
from Classes.tax_inspector import TaxInspector
import sys

# Открываем файл лога для записи (или создаем новый, если он не существует)
log_file_path = 'log.txt'
with open(log_file_path, 'w') as log_file:
    # Сохраняем текущий стандартный вывод
    original_stdout = sys.stdout

    try:
        # Перенаправляем стандартный вывод в файл
        sys.stdout = log_file

        magnit = Market()

        client1 = OrdinaryClient("boris")
        client2 = SpecialClient("prezident", 1)
        client4 = PromotionalClient("Петрович", "free", 100,-100)
        client3 = TaxInspector()

        magnit.acceptToMarket(client1)
        magnit.acceptToMarket(client2)
        magnit.acceptToMarket(client3)
        magnit.acceptToMarket(client4)
        magnit.update()

    finally:
        # Восстанавливаем стандартный вывод
        sys.stdout = original_stdout

