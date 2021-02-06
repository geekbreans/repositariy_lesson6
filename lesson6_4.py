# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False
    _direction = ""

    def __init__(self, name="", color="", speed=0):
        self.name = name
        self.color = color
        self.speed = speed

    def go(self, speed, direction):
        self.speed = speed
        self._direction = direction
        print(f"{self.name} автомобилю назначена скорость движение {self.speed} {self._direction} ")

    def stop(self):
        self.speed = 0
        self._direction = ""
        print("Автомобиль останвился")

    def turn(self, direction):
        self._direction = direction
        print(f"направление движения {direction}")

    def show_speed(self):
        if self.speed == 0:
            print(f'{self.name} "автомобиль стоит"')
        else:
            print(
                f'Автомобиль движется со скорсть {self.speed} {"" if len(self._direction) == 0 else "в напрвлении"} {self._direction}')


class TownCar(Car):
    def show_speed(self):
        if self.speed == 0:
            print(f'{self.name} "автомобиль стоит"')
        else:
            print(
                f'Текущая скорость {self.speed}, {"скорость превышена " if self.speed > 60 else "скорось в ппределах допустимого"}')

    def show_color(self):
        print(f"Цвет машины {self.color}")


class SportCar(Car):
    def show_color(self):
        print(f"Цвет машины {self.color}")


class WorkCar(Car):
    def show_speed(self):
        if self.speed == 0:
            print(f'{self.name} "автомобиль стоит"')
        else:
            print(
                f'Текущая скорость {self.speed}, {"скорость превышена " if self.speed > 40 else "скорось в пределах допустимого"}')

    def show_color(self):
        print(f"Цвет машины {self.color}")


class PoliceCar(Car):
    def __init__(self, name="", color="", speed=0):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = True

    # def s_pol(self, s_bol=True):
    #     self.is_police = s_bol
    def show_color(self):
        print(f"Цвет машины {self.color}")


# c_tc = TownCar("SuperCar", "Red", 0)
# c_tc.go(100, "прямо")
# c_tc.show_speed()


c_tc = SportCar("SportCar", "Red", 0)
c_tc.go(100, "прямо")
c_tc.show_speed()
c_tc.stop()
c_tc.show_speed()
c_tc.show_color()
c_tc.go(100, "влево")
c_tc.show_speed()
print("-------------------------------------------------------------------")
c_pc = PoliceCar("PoliceCar", "Black", 0)
c_pc.go(80, "прямо")
c_pc.show_speed()
c_pc.stop()
c_pc.show_speed()
c_pc.show_color()
c_pc.go(40, "вправо")
c_pc.show_speed()
print("-------------------------------------------------------------------")
c_pc = WorkCar("WorkCar", "Black", 0)
c_pc.go(80, "прямо")
c_pc.show_speed()
c_pc.stop()
c_pc.show_speed()
c_pc.show_color()
c_pc.go(40, "вправо")
c_pc.show_speed()
print("-------------------------------------------------------------------")
c_pc = TownCar("TownCar", "Black", 0)
c_pc.go(70, "влево")
c_pc.show_speed()
c_pc.stop()
c_pc.show_speed()
c_pc.show_color()
c_pc.go(30, "вправо")
c_pc.show_speed()