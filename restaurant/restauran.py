from abc import ABC, abstractmethod


class MenuItem(ABC):
    def __init__(self, name: str, base_price: float):
        self._name = name
        self._base_price = base_price

    @property
    def name(self):
        return self._name

    @property
    def base_price(self):
        return self._base_price

    @abstractmethod
    def calculate_price(self) -> float:
        pass


class Payment_type(ABC):
    @abstractmethod
    def collect_payment(self, amount: float) -> bool:
        pass


class Pizza(MenuItem):
    def __init__(self, name: str, base_price: float, size: str):
        super().__init__(name, base_price)
        self.size = size

    def calculate_price(self) -> float:
        if self.size.lower() == "large":
            return self._base_price * 1.30
        return self._base_price


class Drink(MenuItem):
    def __init__(self, name: str, base_price: float, is_ice: bool):
        super().__init__(name, base_price)
        self.is_ice = is_ice

    @property
    def name(self):
        if self.is_ice:
            return f"{self._name} (со льдом)"
        return self._name

    def calculate_price(self) -> float:
        return self._base_price


class ComboSet(MenuItem):
    def __init__(self, name: str):
        super().__init__(name, 0.0)
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def calculate_price(self) -> float:
        total = sum(item.calculate_price() for item in self.items)
        return total * 0.85  # Скидка 15% на комбо


class CardPayment(Payment_type):
    def __init__(self, card_number: str, expiry_date: str):
        self.card_number = card_number
        self.expiry_date = expiry_date

    def collect_payment(self, amount: float) -> bool:
        if self.expiry_date.strip():
            print(f"\n[УСПЕХ] Списано {amount:.2f} руб. с карты {self.card_number}. Оплата прошла успешно!")
            return True
        else:
            print("\n[ОШИБКА] Недействительный срок карты.")
            return False


class CashPayment(Payment_type):
    def __init__(self):
        pass

    def collect_payment(self, amount: float) -> bool:
        print(f"\n[УСПЕХ] Оплата наличными при получении: {amount:.2f} руб. Заказ принят в обработку.")
        return True


class Order:
    STATUS_NEW = "NEW"
    STATUS_COOKING = "COOKING"
    STATUS_DELIVERING = "DELIVERING"
    STATUS_DELIVERED = "DELIVERED"

    def __init__(self):
        self.__items = []
        self.__status = self.STATUS_NEW

    @property
    def status(self):
        return self.__status

    @property
    def items(self):
        return list(self.__items)

    def next_step(self):
        if self.__status == self.STATUS_NEW:
            self.__status = self.STATUS_COOKING
            print("\n>> Статус заказа изменен на: Готовится (COOKING)")
        elif self.__status == self.STATUS_COOKING:
            self.__status = self.STATUS_DELIVERING
            print("\n>> Статус заказа изменен на: Доставляется (DELIVERING)")
        elif self.__status == self.STATUS_DELIVERING:
            self.__status = self.STATUS_DELIVERED
            print("\n>> Статус заказа изменен на: Доставлен (DELIVERED)")
        elif self.__status == self.STATUS_DELIVERED:
            print("\n>> Заказ уже доставлен и закрыт!")

    def add_item(self, item: MenuItem):
        if self.__status != self.STATUS_NEW:
            print("\n[ОШИБКА] Нельзя добавить блюдо: заказ уже готовится или доставляется!")
            return
        self.__items.append(item)
        print(f"\n[УСПЕХ] Добавлено в корзину: {item.name}")

    def get_total_cost(self) -> float:
        return sum(item.calculate_price() for item in self.__items)

    def pay(self, payment_method: Payment_type) -> bool:
        amount = self.get_total_cost()
        if amount == 0:
            print("\n[ОШИБКА] Ваша корзина пуста! Добавьте блюда перед оплатой.")
            return False
        print(f"\nИнициирована оплата на сумму: {amount:.2f} руб.")
        return payment_method.collect_payment(amount)