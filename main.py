import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("Приветствую. Это отображение графика изменения графика пути от времени.")
acceleration = input("Введите ускорение:")
if 'неизвестно' in acceleration:
    acceleration = 0
else:
    acceleration = float(acceleration)
path = input("Введите продолжительность пути:")
if 'неизвестно' in path:
    path = 0
else:
    path = float(path)
speed = input('Введите начальую скорость:')
if 'неизвестно' in speed:
    speed = 0
else:
    speed = float(path)

if acceleration >= 0:
    a = True
    while a:
        time = input("Введите продолжительность времени пути:")
        if float(time) < 0:
            print("Некорректный ввод")
        elif float(time) == 0:
            print("Время = 0, путь = 0")
            exit()
        elif float(time) > 0:
            time = float(time)
            a = False
        else:
            print("Некорректный ввод")
if acceleration < 0:
    time = speed / ((-1)*acceleration)
i = 0.01
while True:
    if i <= time < i * 10:
        break
    i *= 10
a = []
for j in range(0, 11):
    if i * j > time:
        s = speed * time + (acceleration * (time ** 2)) / 2
        if s < path:
            a.append(s)
        break
    else:
        s = speed * j * i + (acceleration * ((j * i) ** 2)) / 2
        if s > path:
            break
    a.append(s)
a[0] = 0
data = {'series1': a
        }
df = pd.DataFrame(data)
x = np.arange(10)  # numpy.arange([start, ]stop, [step, ]dtype=None)
plt.axis([0, time + 1, 0, a[9]])  # xmin, xmax, ymin, ymax = axis([xmin, xmax, ymin, ymax])
plt.plot(x, df)
plt.legend(data, loc=2)
plt.show()
