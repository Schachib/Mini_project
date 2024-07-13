class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender

    def display_info(self):
        return (f'Имя: {self.first_name}, Фамилия: {self.second_name}, Пол:'
                f' {self.gender}, Отпускных дней в году: {self.vacation_days}.')

# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee('Khabib', 'Shamkhalov', 'м')
employee2 = Employee('Хабиб', 'Шамхалов', "м")

# Вывод информации о сотрудниках.
print(employee1.display_info())
print(employee2.display_info())
