class Phone:
    # Объявление объекта класса
    line_type = 'проводной'

    # Это инициализатор класса, в котором объявлено два параметра.
    def __init__(self, dial_type_value='Брак') -> None:
        self.dial_type = dial_type_value  # это атрибут объекта
        print(self.__dict__)


rotary_phone = Phone(dial_type_value='дисковый')
keypad_phone = Phone(dial_type_value='кнопочный')
voice_phone = Phone(dial_type_value='голосовой')


