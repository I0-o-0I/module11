import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani
from matplotlib.animation import  ArtistAnimation

#Matplotlib — это комплексная библиотека для создания статичных, анимированных и интерактивных визуализаций на Python.
#plt.plot() — стандартная функция, которая строит график в соответствии со значениями, которые ей были переданы.
#plt.show() — функция, которая отвечает за вывод визуализированных данных на экран.

t=np.arange(0, 2*np.pi, 0.01)
x=16*np.sin(t)**3
y=13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
plt.plot(x, y, 'r--') #r-- красная линия пунктирная
plt.xlabel('X', color = 'green') #подпись для оси х
plt.ylabel('Y', size = 15) #подпись для оси у

#С помощью класса ArtistAnimation анимация создается на основе уже готового списка объектов для каждого кадра.
fig = plt.figure(figsize=(10,6))
ax=fig.add_subplot(projection='3d') #3d ось
x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y = np.arange(-2*np.pi, 2*np.pi, 0.2)
x, y = np.meshgrid(x, y) #формирование двумерной сетки координат x и y

#список для изменяемого параметра и коллекция для хранения объектов Artist:
phasa = np.arange(0, 2*np.pi, 0.01)
frames =[]

#формирование объектов Artist
for i in phasa:
    z =np.sin(x+i)
    line = ax.plot_surface(x, y, z, cmap = 'PiYG')
    frames.append([line])
anim = ArtistAnimation(fig, frames, interval=30, blit=True, repeat=True)
plt.show()