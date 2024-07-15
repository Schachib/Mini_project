class Phone:
    # Настройки телефона
    # Родительский класс
    line_type = 'проводной'

    def __init__(self, dial_type_value) -> None:
        self.dial_type = dial_type_value  # это атрибут объекта

    def dial_type_upgrade(self, new_dial_type):
        # Измененние типа телефона
        self.dial_type = new_dial_type

    def ring(self):
        # Звонок
        print('Дззынь~')

    def call(self, phone_number):
        # Вызов звонка
        print(f'Входящий звонок c номера {phone_number}!', end=' ')
        print(f'Тип связи - {self.line_type}.')

    def get_missed_call(self):
        # Получение кол-ва пропузенных звонков
        print('Запрос кол-ва пропузенных звонков.')

    def __str__(self) -> str:
        # Вывод объекта
        return f'Это {self.line_type} телефон. Набор - {self.dial_type}.'


class MobilePhone(Phone):
    # Дочерний класс
    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    def __init__(self, dial_type_value, network_type) -> None:
        self.network_type = network_type
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзынь-Дзынь!')

    def start_game(self):
        print('Игра запущена!')


rotary_phone = Phone(dial_type_value='дисковый')
print(rotary_phone)
mobile_phone = MobilePhone(dial_type_value='сенсорный', network_type='LTE')

mobile_phone.start_game()
print(mobile_phone)
print(mobile_phone.battery_type)
