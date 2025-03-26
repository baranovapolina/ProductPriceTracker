import csv
from datetime import datetime, timedelta

class ProductPriceTracker:
    """
    Клас для обробки змін цін товарів за останній місяць
    """
    
    def __init__(self, file_path):
        """
        Ініціалізуємо клас з шляхом до файлу
        """
        self.file_path = file_path
        self.data = self.read_file()

if __name__ == "__main__":
    tracker = ProductPriceTracker("products.txt")
    product = input("Введіть назву товару: ")
    print(tracker.get_price_change(product))
