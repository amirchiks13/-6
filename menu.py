def get_restaurant_menu():

    return [
        {"type": "pizza", "name": "Пепперони", "price": 600.0},
        {"type": "pizza", "name": "Маргарита", "price": 450.0},
        {"type": "pizza", "name": "Четыре сыра", "price": 700.0},
        {"type": "drink", "name": "Кока-Кола", "price": 150.0},
        {"type": "drink", "name": "Апельсиновый сок", "price": 180.0},
        {"type": "combo", "name": "Комбо 'Обед студента' (Маргарита + Кола)", "items": [
            ("pizza", "Маргарита", 450.0, "small"),
            ("drink", "Кока-Кола", 150.0, False)
        ]},
        {"type": "combo", "name": "Комбо 'Семейный'(Пепперони+Апельсиновый сок)", "items": [
            ("pizza", "Пепперони", 600.0, "large" ),
            ("drink", "Апельсиновый сок", 180.0, False)
        ]}
    ]