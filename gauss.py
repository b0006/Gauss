# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import random

#функция решения СЛАУ методом Гаусса
def seidel(A, b, eps):
    n = len(A)
    answers = [.0 for i in range(n)]

    converge = False
    while not converge:
        x_new = np.copy(answers)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * answers[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = sqrt(sum((x_new[i] - answers[i]) ** 2 for i in range(n))) <= eps
        answers = x_new

    return answers

#---------------------------------------------
#формируем систему уравнений
#random_x = np.array([np.random.randint(-5, 10, 5)])
#random_y = np.array([np.random.randint(-5, 10, 5)])

A_mas = np.zeros((3, 3)) #двумерный массив 3 на 3(часть матрицы А)
b_mas = np.zeros((3, 1)) #одномерный массив (часть матрицы B)

#формируем F(a)
#for i in range(5):
A_mas[0][0] = 10642
A_mas[0][1] = 1134
A_mas[0][2] = 130
b_mas[0] = 1712

#формируем F(b)
#for i in range(5):
A_mas[1][0] = 1134
A_mas[1][1] = 130
A_mas[1][2] = 18
b_mas[1] = 196

#формируем F(c)
#for i in range(5):
A_mas[2][0] = 130
A_mas[2][1] = 18
A_mas[2][2] = 5
b_mas[2] = 25

#получаем решение системы уравнения
answers = seidel(A_mas, b_mas, 0.001)

for i in range(3):
    print("x[", i + 1, "]", answers[i])

#статичная выборка
x_vyborka = np.array([[0], [1], [2], [5], [10]])
y_vyborka = np.array([[-1], [0], [3], [8], [15]])

kvadro = np.zeros((5, 1))

#подставляем решение в квадратное уравнение
for i in range(5):
    kvadro[i] = pow(x_vyborka[i], 2) * answers[0] + x_vyborka[i] * answers[1] + answers[2]

#рисуем график
fig, ax = plt.subplots()
ax.plot(x_vyborka, y_vyborka, color="blue", label="Старый") #граф со статическими параметрами
ax.plot(x_vyborka, kvadro, color="red", label="Новый")      #граф, где параметры вычислены методом Гаусса

ax.set_xlabel("x")
ax.set_ylabel("y") 

ax.legend() 

ax.plot(x_vyborka, y_vyborka, x_vyborka, y_vyborka, 'bo') # рисуем точки
ax.plot(x_vyborka, kvadro, x_vyborka, kvadro, 'ro')
ax.set_title(r'$Графики$')      
ax.grid(True) 

plt.show()
