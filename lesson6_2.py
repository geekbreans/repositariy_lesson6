# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода
class Road:
    _length = 0
    _width = 0

    def __init__(self, length=0.0, width=0.0):
        self._length = float(length)
        self._width = float(width)

    def calculate(self):
        return self._length * self._width * 0.25


r_wr = Road(80, 90)
print(r_wr.calculate())
