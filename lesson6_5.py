# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str = ""
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print(f"Ручка фирмы {self.title} начинает писать плавно")


class Pencil(Stationery):
    def draw(self):
        print(f"Карандаш фирмы {self.title} начинает рисовать красивые узоры")

class Handle(Stationery):
    def draw(self):
        print(f"Маркер фирмы {self.title} начинает наность специальные символы")


c_pe = Pen ("BIG")
c_pe.draw()
print("-------------------------------------------------------------------")
c_pe = Pencil("Sako and Vancenti")
c_pe.draw()
print("-------------------------------------------------------------------")
c_pe = Handle("Best Marker")
c_pe.draw()
