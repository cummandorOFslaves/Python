import numpy as np
print('введите тип матрицы:3(3х3), 2(2х2),1/2(1x2),2/1(2x1),1/3(1x3),3/1(3x1) ')
b=input()
while b=='3':
    print('введите тип операции: определитель(det),умножение(*),транспонирование(tran)')
    g = input()
    if g=='*':
        print('введите тип второй матрицы для умножения 1(3х3),2(3х1)')
        b=input()
        while b=='1':
            print('введите данные 1 матрицы')
            a1, a2, a3 = map(int, input().split())
            a4, a5, a6 = map(int, input().split())
            a7, a8, a9 = map(int, input().split())
            print('введите данные 2 матрицы')
            b1, b2, b3 = map(int, input().split())
            b4, b5, b6 = map(int, input().split())
            b7, b8, b9 = map(int, input().split())
            a = np.array([[a1, a2, a3], [a4, a5, a6], [a7, a8, a9]])
            b = np.array([[b1, b2, b3], [b4, b5, b6], [b7, b8, b9]])
            r1 = np.dot(a, b)
            print("Результат умножения функцией:\n", r1)
            break
        while b=='2':
            print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
            a1, a2, a3 = map(int, input().split())
            a4, a5, a6 = map(int, input().split())
            a7, a8, a9 = map(int, input().split())
            print('введите данные 2 матрицы')
            b1=int(input())
            b4=int(input())
            b7=int(input())
            a = np.array([[a1, a2, a3], [a4, a5, a6], [a7, a8, a9]])
            b = np.array([[b1], [b4], [b7]])
            r1 = np.dot(a, b)
            print(r1)
            break

    elif g=='det':
        a1, a2,a3 = map(int, input().split())
        a4, a5,a6 = map(int, input().split())
        a7,a8,a9=map(int,input().split())
        M = [[a1, a2,a3], [a4, a5,a6],[a7,a8,a9]]
        print(np.linalg.det(M))
    elif g=='tran':
        print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
        a1, a2, a3 = map(int, input().split())
        a4, a5, a6 = map(int, input().split())
        a7, a8, a9 = map(int, input().split())
        a = np.array([[a1, a2,a3], [a4, a5,a6],[a7,a8,a9]])
        a = a.transpose()
        print(a)
    break
while b=='2':
    print('введите тип операции: определитель(det),умножение(*),транспонирование(tran)')
    g = input()
    print()
    if g=='*':
        print('введите тип второй матрицы для умножения 1(2х2),2(2х1)')
        b = input()
        while b=='1':
            print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
            a1, a2 = map(int, input().split())
            a4, a5 = map(int, input().split())
            print('введите данные 2 матрицы')
            b1, b2 = map(int, input().split())
            b3, b4 = map(int, input().split())
            a = np.array([[a1, a2], [a4, a5]])
            b = np.array([[b1, b2], [b3, b4]])
            r1 = np.dot(a, b)
            print("Результат умножения функцией:\n", r1)
            break
        while b=='2':
            print('введите данные 1 матрицы')
            a3, a4 = map(int, input().split())
            a5, a6 = map(int, input().split())
            print('введите данные 2 матрицы')
            a1=int(input())
            a2=int(input())
            a = np.array([[a3, a4], [a5, a6]])
            b = np.array([[a1], [a2]])
            r1 = np.dot(a, b)
            print(r1)
            break
    elif g=='det':
        print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
        a1, a2 = map(int, input().split())
        a3, a4 = map(int, input().split())
        M = [[a1, a2], [a3, a4]]
        print(np.linalg.det(M))
    elif g=='tran':
        print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
        a1,a2=map(int,input().split())
        a3,a4=map(int,input().split())
        a = np.array([[a1, a2], [a3,a4]])
        a = a.transpose()
        print(a)
    break
while b=='1/2':
    print('введите тип операции: умножение(*),транспонирование(tran)')
    g = input()
    if g=='*':
        print('введите данные 1 матрицы(1x2) через пробел,по окончанию ввода строки нажмите enter')
        a1, a2 = map(int, input().split())
        print('введите данные 2 матрицы(2x1) через  enter')
        a3 = int(input())
        a4 = int(input())
        a = np.array([[a1, a2]])
        b = np.array([[a3], [a4]])
        r1 = np.dot(a, b)
        print("Результат умножения функцией:\n", r1)
        break
    elif g=='tran':
        print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
        a1, a2 = map(int, input().split())
        a = np.array([[a1], [a2]])
        a = a.transpose()
        print(a)
        break
    break
while b=='2/1':
    print('введите тип операции: умножение(*),транспонирование(tran)')
    g = input()
    if g=='*':
        print('введите данные 1 матрицы(2x1) через enter')
        a3 = int(input())
        a4 = int(input())
        print('введите данные 2 матрицы(1x2) через пробел,по окончанию ввода строки нажмите enter')
        a1, a2 = map(int, input().split())
        a = np.array([[a3], [a4]])
        b = np.array([[a1, a2], ])
        r1 = np.dot(a, b)
        print(r1)
        break
    elif g=='tran':
        print('введите данные 1 матрицы(2x1) через enter')
        a1=int(input())
        a2 = int(input())
        a = np.array([[a1], [a2]])
        a = a.transpose()
        print(a)
    break
while b=='1/3':
    print('введите тип операции: умножение(*),транспонирование(tran)')
    g = input()
    if g=='*':
        print('введите данные 1 матрицы(1x3) через пробел,по окончанию ввода строки нажмите enter')
        a1, a2,a3 = map(int, input().split())
        print('введите данные 2 матрицы(3x1) через  enter')
        a4 = int(input())
        a5 = int(input())
        a6=int(input())
        a = np.array([[a1, a2,a3]])
        b = np.array([[a4], [a5],[a6]])
        r1 = np.dot(a, b)
        print("Результат умножения функцией:\n", r1)
        break
    elif g=='tran':
        print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
        a1, a2, a3 = map(int, input().split())
        a = np.array([[a1, a2, a3]])
        a = a.transpose()
        print(a)
    break
while b=='3/1':
    print('введите тип операции: умножение(*),транспонирование(tran)')
    g = input()
    if g=='*':
        print('введите данные 1 матрицы(3x1) через  enter')
        a1=int(input())
        a2=int(input())
        a3=int(input())
        print('введите данные 2 матрицы(1x3) через   enter')
        a4,a5,a6 = map(int,input().split())
        a = np.array([[a1], [a2],[a3]])
        b = np.array([[a4, a5,a6]])
        r1 = np.dot(a, b)
        print(r1)
    elif g=='tran':
        print('введите данные 1 матрицы через enter')
        a1 = int(input())
        a2 = int(input())
        a3 = int(input())
        a = np.array([[a1], [a2],[a3]])
        a = a.transpose()
        print(a)
    break