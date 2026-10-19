class Animal:
    def __init__(self, name, age, type, size, eat):
        self.name = name
        self.age = age
        self.type = type
        self.size = size
        self.eat = eat

    def make_sound(self, sound):
       return f"{self.name} издает звук: {sound}!"

    def dont_eat(self, noeat):
        return f"{self.name} не ест: {noeat}"

class Amphibians(Animal):
    def __init__(self, name, age, type, size, eat, often_live, color):
        super().__init__(name, age, type, size, eat)
        self.live = often_live
        self.color = color
        

    def sing(self, sing):
        return f"{self.name} может спеть: {sing}"

    def trick(self, trick):
        return f"{self.name} может выполнить: {trick}"

amphibian1 = Amphibians(name='Квака', age=2, type='Лягушка', size='Маленький', eat='Насекомые', often_live='У водоема', color='Зеленый')
amphibian2 = Amphibians(name='Блэйз', age=4, type='Саламандра', size='Средний', eat='Черви', often_live='Лес', color='Черно-желтый')
amphibian3 = Amphibians(name='Лунтик', age=1, type='Аксолотль', size='Маленький', eat='Рачки', often_live='Вода', color='Розовый')
class Reptiles(Animal):
    def __init__(self, name, age, type, size, eat, venomus, legs):
        super().__init__(name, age, type, size, eat)
        self.venom = venomus
        self.legs = legs

    def move(self, move):
        return f"{self.name} сделает: {move}"

    def dangerous(self, danger):
        return f"{self.name} атакует с помощью {danger}"
reptile1 = Reptiles(name='Нага', age=3, type='Кобра', size='Крупный', eat='Грызуны', venomus=True, legs=0)
reptile2 = Reptiles(name='Гена', age=8, type='Крокодил', size='Огромный', eat='Мясо', venomus=False, legs=4)
reptile3 = Reptiles(name='Тортила', age=25, type='Черепаха', size='Средний', eat='Растения', venomus=False, legs=4)
    
class ZooShow:
    def __init__(self):
        print(f"ДОБРО ПОЖАЛОВАТЬ В ЗОО-ШОУ!\n")
        self.start_show()

    def start_show(self):
        print("Выберите программу шоу:")
        print("1 - Шоу Земноводных (Amphibians)")
        print("2 - Шоу Пресмыкающихся (Reptiles)")

        choice = input("Введите номер шоу (1 или 2): ").strip()

        if choice == '1':
            self.amphibians_show()
        elif choice == '2':
            self.reptiles_show()
        else:
            print("Неверный выбор! Попробуйте снова.")
            self.start_show()   

    def amphibians_show(self):
        print("\n" + "~" * 15 + " ШОУ ЗЕМНОВОДНЫХ " + "~" * 15)
        
        print(f"1. {amphibian1.type} {amphibian1.name}: {amphibian1.trick('прыжок через обруч под водой')}")
        print(f"2. {amphibian2.type} {amphibian2.name}: {amphibian2.sing('вечернюю серенаду дождя')}")
        print(f"3. {amphibian3.type} {amphibian3.name}: {amphibian3.make_sound('тихий подводный бульк')}")
        self.buy_tickets("Шоу Земноводных")
        choice_show = input("Какое представление вы хотите посмотреть: ")
        choice_show = input("Какое представление вы хотите посмотреть (1-3): ").strip()
        if choice_show == '1':
            show_item = f"1. {amphibian1.type} {amphibian1.name}: {amphibian1.trick('прыжок через обруч под водой')}"
        elif choice_show == '2':
            show_item = f"2. {amphibian2.type} {amphibian2.name}: {amphibian2.sing('вечернюю серенаду дождя')}"
        elif choice_show == '3':
            show_item = f"3. {amphibian3.type} {amphibian3.name}: {amphibian3.make_sound('тихий подводный бульк')}"
    def reptiles_show(self):
        print(f"\nШОУ ПРЕСМЫКАЮЩИХСЯ ")
        
        print(f"1. {reptile1.type} {reptile1.name}: станцует под звуки флейты!")
        print(f"2. {reptile2.type} {reptile2.name}: покажет мастер-класс по открыванию пасти и плаванию!")
        print(f"3. {reptile3.type} {reptile3.name}: устроит медленные гонки на арене!")
        self.buy_tickets("Шоу Пресмыкающихся")
        choice_show = input("\nКакое представление вы хотите посмотреть (1-3): ").strip()
        if choice_show == '1':
            selected_show = f"{reptile1.type} {reptile1.name}: станцует под звуки флейты!"
        elif choice_show == '2':
            selected_show = f"{reptile2.type} {reptile2.name}: покажет мастер-класс по открыванию пасти и плаванию!"
        elif choice_show == '3':
            selected_show = f"{reptile3.type} {reptile3.name}: устроит медленные гонки на арене!"
    def buy_tickets(self, show_name):
        print(f"\n ПОКУПКА БИЛЕТОВ ")
        print("Цены на билеты:")
        print("  [1] Обычное место — 500 руб.")
        print("  [2] VIP место (лучший обзор + фото с животным) — 1500 руб.")
        seat_choice = input("\nВыберите тип места (1 или 2): ").strip()

        if seat_choice == '1':
            seat_type = "Обычное"
            total_price = 500
        elif seat_choice == '2':
            total_price = 1500
            seat_type = "VIP"

        else:
            seat_type = "Обычное (по умолчанию)"
            total_price = 500

        print(f"\nВЫ УСПЕШНО КУПИЛИ БИЛЕТЫ НА: {show_name.upper()}!")
        print(f"Категория места: {seat_type}")
        print(f"Общая стоимость: {total_price} руб.\n")
        print(f'"{show_name}"')
        print(f"Выбранный номер: {selected_show}\n")

show = ZooShow()