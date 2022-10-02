print('введите тип матрицы:3(3х3), 2(2х2),1/2(1x2),2/1(2x1),1/3(1x3),3/1(3x1) ')
b=input()
while b=='3':
    print('введите тип операции: определитель(det),умножение(*),транспонирование(tran)')
    g = input()
    if g=='*':
        print('введите тип второй матрицы для умножения 1(3х3),2(3х1)')
        b=input()
        while b=='1':
            print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
            a1,a2,a3=map(int,input().split())
            a4,a5,a6=map(int,input().split())
            a7,a8,a9=map(int,input().split())
            print('введите данные 2 матрицы')
            a10,a11,a12=map(int,input().split())
            a13,a14,a15=map(int,input().split())
            a16,a17,a18=map(int,input().split())
            c1=a1*a10+a2*a13+a3*a16
            c2=a1*a11+a2*a14+a3*a17
            c3=a1*a12+a2*a15+a3*a18
            c4=a4*a10+a5*a13+a6*a16
            c5=a4*a11+a5*a14+a6*a17
            c6=a4*a12+a5*a15+a6*a18
            c7=a7*a10+a8*a13+a9*a16
            c8=a7*a11+a8*a14+a9*a17
            c9=a7*a12+a8*a15+a9*a18
            matrix3=[c1,c2,c3,c4,c5,c6,c7,c8,c9]
            print(matrix3[0],matrix3[1],matrix3[2])
            print(matrix3[3],matrix3[4],matrix3[5])
            print(matrix3[6],matrix3[7],matrix3[8])
            break
        while b=='2':
            print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
            a1, a2, a3 = map(int, input().split())
            a4, a5, a6 = map(int, input().split())
            a7, a8, a9 = map(int, input().split())
            print('введите данные 2 матрицы')
            a10=int(input())
            a11=int(input())
            a12=int(input())
            c1=a1*a10+a2*a11+a3*a12
            c2=a4*a10+a5*a11+a6*a12
            c3=a7*a10+a8*a11+a9*a12
            print(c1)
            print(c2)
            print(c3)
            break



    elif g=='det':
        print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
        a1, a2, a3 = map(int, input().split())
        a4, a5, a6 = map(int, input().split())
        a7, a8, a9 = map(int, input().split())
        det=a1*a5*a9+a8*a3*a4+a7*a2*a6-a7*a5*a3-a1*a6*a8-a9*a4*a2
        print(det)
    elif g=='tran':
        print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
        a1, a2, a3 = map(int, input().split())
        a4, a5, a6 = map(int, input().split())
        a7, a8, a9 = map(int, input().split())
        print(a1,a4,a7)
        print(a2,a5,a8)
        print(a3,a6,a9)
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
            a10, a11 = map(int, input().split())
            a13, a14 = map(int, input().split())
            c1=a1*a10+a2*a13
            c2=a1*a11+a2*a14
            c3=a4*a10+a5*a13
            c4=a4*a11+a5*a14
            matrix3=[c1,c2,c3,c4]
            print(matrix3[0],matrix3[1])
            print(matrix3[2],matrix3[3])
            break
        while b=='2':
            print('введите данные 1 матрицы')
            a3, a4 = map(int, input().split())
            a5, a6 = map(int, input().split())
            print('введите данные 2 матрицы')
            a1=int(input())
            a2=int(input())
            c1=a3*a1+a4*a2
            c2=a5*a1+a6*a2
            print(c1)
            print(c2)
    elif g=='det':
        print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
        a1, a2 = map(int, input().split())
        a4, a5 = map(int, input().split())
        det=a1*a5-a4*a2
        print(det)
    elif g=='tran':
        print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
        a1,a2=map(int,input().split())
        a3,a4=map(int,input().split())
        print(a1,a3)
        print(a2,a4)
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
        c1 = a1 * a3 + a2 * a4
        matrix3 = c1
        print(matrix3)
    elif g=='tran':
        print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
        a1, a2 = map(int, input().split())
        print(a1)
        print(a2)
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
        c1 = a1 * a3 + a2 * a4
        matrix3 = c1
        print(matrix3)
    elif g=='tran':
        print('введите данные 1 матрицы(2x1) через enter')
        a1=int(input())
        a2 = int(input())
        print(a1,a2)
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
        c1 = a1 * a4 + a2 * a5+a3*a6
        print(c1)
    elif g=='tran':
        print('введите данные 1 матрицы через пробел,по окончанию ввода строки нажмите enter')
        a1, a2,a3 = map(int, input().split())
        print(a1)
        print(a2)
        print(a3)
    break
while b=='3/1':
    print('введите тип операции: умножение(*),транспонирование(tran)')
    g = input()
    if g=='*':
        print('введите данные 1 матрицы(3x1) через  enter')
        a1=int(input())
        a2=int(input())
        a3=int(input())
        print('введите данные 2 матрицы(3x1) через   enter')
        a4,a5,a6 = map(int,input().split())
        c1 = a1 * a4 + a2 * a5+a3*a6
        print(c1)
    elif g=='tran':
        print('введите данные 1 матрицы через enter')
        a1 = int(input())
        a2 = int(input())
        a3 = int(input())
        print(a1,a2,a3)
    break


