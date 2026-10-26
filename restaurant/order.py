
from menu import get_restaurant_menu
from restauran import CardPayment, CashPayment, ComboSet, Drink, Order, Pizza

if __name__ == "__main__":
    order = Order()
    catalog = get_restaurant_menu()

    print("=== ДОБРО ПОЖАЛОВАТЬ В ОНЛАЙН-РЕСТОРАН ===")

    while True:
        print("\n--- ГЛАВНОЕ МЕНЮ ---")
        print(f"Текущий статус заказа: {order.status}")
        print("1. Посмотреть меню ресторана и добавить блюдо")
        print("2. Посмотреть корзину (общая стоимость)")
        print("3. Перевести заказ на следующий этап (next_step)")
        print("4. Оплатить заказ")
        print("5. Выйти из программы")

        choice = input("Выберите пункт меню (1-5): ").strip()

        if choice == "1":
            if order.status != Order.STATUS_NEW:
                print(
                    "\n[ОШИБКА] Нельзя добавлять блюда — заказ уже обрабатывается!"
                )
                continue

            print("\n--- МЕНЮ РЕСТОРАНА ---")
            for idx, item_data in enumerate(catalog, 1):
                if item_data["type"] == "pizza":
                    print(
                        f"{idx}. Пицца '{item_data['name']}' — {item_data['price']} руб. (Базовая)"
                    )
                elif item_data["type"] == "drink":
                    print(
                        f"{idx}. Напиток '{item_data['name']}' — {item_data['price']} руб."
                    )
                elif item_data["type"] == "combo":
                    print(
                        f"{idx}. Комбо-набор: {item_data['name']} (Скидка 15%)"
                    )

            try:
                item_choice = (
                    int(input("Введите номер позиции для заказа: ")) - 1
                )
                if item_choice < 0 or item_choice >= len(catalog):
                    print("Неверный номер позиции.")
                    continue
            except ValueError:
                print("Ошибка: введите число!")
                continue

            selected = catalog[item_choice]


            if selected["type"] == "pizza":
                size_choice = (
                    input("Выберите размер (small / medium / large): ")
                    .strip()
                    .lower()
                )
                if size_choice not in ["small", "medium", "large"]:
                    size_choice = "medium"
                dish = Pizza(selected["name"], selected["price"], size_choice)
                order.add_item(dish)

            elif selected["type"] == "drink":
                ice_input = input("Добавить лёд? (да/нет): ").strip().lower()
                is_ice = ice_input in ["да", "yes", "y", "1"]
                dish = Drink(selected["name"], selected["price"], is_ice)
                order.add_item(dish)

            elif selected["type"] == "combo":
                combo = ComboSet(selected["name"])
                for sub_type, sub_name, sub_price, sub_attr in selected[
                    "items"
                ]:
                    if sub_type == "pizza":
                        combo.add_item(Pizza(sub_name, sub_price, sub_attr))
                    elif sub_type == "drink":
                        combo.add_item(Drink(sub_name, sub_price, sub_attr))
                order.add_item(combo)

        elif choice == "2":
            print(
                f"\n--> Общая стоимость текущего заказа: {order.get_total_cost():.2f} руб."
            )
            items_list = order.items
            if items_list:
                print("Состав заказа:")
                for item in items_list:
                    print(f" - {item.name}: {item.calculate_price():.2f} руб.")
            else:
                print(" Корзина пуста.")

        elif choice == "3":
            order.next_step()

        elif choice == "4":
            print("\nВыберите способ оплаты:")
            print("1. Банковская карта")
            print("2. Наличные при получении")
            pay_choice = input("Ваш выбор (1-2): ").strip()

            if pay_choice == "1":
                card_num = input("Введите номер карты: ")
                expiry = input("Введите срок действия (например, 12/28): ")
                payment = CardPayment(card_num, expiry)
                order.pay(payment)
            elif pay_choice == "2":
                payment = CashPayment()
                order.pay(payment)
            else:
                print("Неверный способ оплаты.")

        elif choice == "5":
            print("Спасибо за использование онлайн-ресторана! До свидания.")
            break
        else:
            print("Неверный пункт меню, выберите число от 1 до 5.")