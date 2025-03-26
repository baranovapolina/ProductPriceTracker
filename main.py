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

    def read_file(self):
        """
        Зчитує дані з файлу та повертає список словників
        """
        data = []
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) != 3:
                        continue
                    name, date, price = row
                    try:
                        date = datetime.strptime(date, "%Y-%m-%d")
                        price = float(price)
                        data.append({"name": name, "date": date, "price": price})
                    except ValueError:
                        continue
        except FileNotFoundError:
            print("Файл не знайдено")
        return data

    def get_price_change(self, product_name):
         """
        Повертає зміну ціни на товар за останній місяць
        """

        
        last_month = datetime.now() - timedelta(days=30)
        prices = [item["price"] for item in self.data if item["name"] == product_name and item["date"] >= last_month]
        last_month = datetime.now() - timedelta(days=30)
        prices = [item["price"] for item in self.data if item["name"] == product_name and item["date"] >= last_month]
        
        if len(prices) < 2:
            return "Недостатньо даних для аналізу"

        return f"Зміна ціни за місяць: {prices[-1] - prices[0]} грн"

if __name__ == "__main__":
    tracker = ProductPriceTracker("products.txt")
    product = input("Введіть назву товару: ")
    print(tracker.get_price_change(product))
