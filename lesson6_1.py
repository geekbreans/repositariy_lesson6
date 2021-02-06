import time
import sys
import os


class TrafficLight:
    __color = {'red': 7, 'yelow': 3, 'green': 1}
    __colorforprint = {'red': "\033[1;31m", 'yelow': "\033[1;33m", 'green': "\033[1;32m"}

    def running(self, set_seconds=4):
        self.__color['green'] = set_seconds
        w_value = self._chekcfileexist()
        while w_value:
            w_value = self._chekcfileexist()

            for el in self.__color:
                sys.stdout.write(self.__colorforprint[el])
                print(f'Светофор включил {el} цвет, длитетельность {self.__color[el]} секунд')
                # print(self.__color[el])
                time.sleep(self.__color[el])

    def _chekcfileexist(self):
        w_value = False
        if os.path.exists("TrafficLightWork.txt"):
            w_value = True
        return w_value


w_tf = TrafficLight()
print("Программа по управлению cветоформ будет работать, пока в рабочей папке имеется файл с наименованием - "
      "TrafficLightWork.txt")
w_tf.running(4)
print("Работа программы по управлению светоформ  закончена, файл с наименованием - TrafficLightWork.txt, отсутсвует в "
      "рабочей папке")
