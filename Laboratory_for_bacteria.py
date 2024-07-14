class BacteriaProducer:
    # Допишите инициализатор класса
    def __init__(self, max_bacteria=0):
        self.max_bacteria = max_bacteria
        self.number_bacteria = 0

    def create_new(self):
        if self.number_bacteria < self.max_bacteria:
            self.number_bacteria += 1
            print('Добавлена одна бактерия. '
                  f'Количество бактерий в популяции: {self.number_bacteria}')
        else:
            print('Нет места под новую бактерию')

    # Допишите метод
    def remove_one(self):
        if self.number_bacteria > 0:
            self.number_bacteria -= 1
            print('Одна бактерия удалена. '
                  f'Количество бактерий в популяции: {self.number_bacteria}')
        else:
            print('В популяции нет бактерий, удалять нечего')


# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()
