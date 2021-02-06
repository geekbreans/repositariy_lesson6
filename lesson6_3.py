# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, wage=0.0, bonus=0.0):
        self._income["wage"] = float(wage)
        self._income["bonus"] = float(bonus)

    @property
    def income(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


# m_wrk = Worker()
# print(m_wrk.income)

m_posit = Position(10000, 20000)
m_posit.name = "Petr"
m_posit.surname = "Pupkin"
print(f'Сотрудник {m_posit.get_full_name()}, имеет итоговую оплату за работу в размере {m_posit.get_total_income()} рублей')

