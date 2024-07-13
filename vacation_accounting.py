class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days

    def consume_vacation(self, vacation_days_spent):
        self.remaining_vacation_days -= vacation_days_spent

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

    def display_info(self):
        return (f'Имя: {self.first_name}, Фамилия: {self.second_name}, Пол:'
                f' {self.gender}, Отпускных дней в году: {self.vacation_days}.')


# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee('Khabib', 'Shamkhalov', 'м')
employee2 = Employee('Хабиб', 'Шамхалов', "м")

# Вывод информации о сотрудниках.
employee1.consume_vacation(7)
print(employee1.get_vacation_details())
