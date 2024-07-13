class Phone:
    # Настройки телефона
    line_type = 'проводной'

    def __init__(self, dial_type_value='Брак') -> None:
        self.dial_type = dial_type_value  # это атрибут объекта
        print(self.__dict__)

    def dial_type_upgrade(self, new_dial_type):
        # Измененние типа телефона
        self.dial_type = new_dial_type

    def ring(self):
        print('Дззынь~')

    def call(self, phone_number):
        print(f'Входящий звонок c номера {phone_number}!', end=' ')
        print(f'Тип связи - {self.line_type}.')

    def get_missed_call(self):
        print('Запрос кол-ва пропузенных звонков.')


rotary_phone = Phone(dial_type_value='дисковый')
keypad_phone = Phone(dial_type_value='кнопочный')
voice_phone = Phone(dial_type_value='голосовой')

rotary_phone.ring()
rotary_phone.call('234-5678')
rotary_phone.get_missed_call()
rotary_phone.dial_type_upgrade('дисковый')
print(rotary_phone.dial_type)
