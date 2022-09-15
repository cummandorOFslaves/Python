import math


'''Сложение, вычитание, умножение, деление, возведение в степень, логарифм,
округление в большую сторону до N знака после запятой, округление в меньшую сторону
до N знака после запятой.'''

while True:
    q = input('Выберите действие(+,-,*,/,^,log,up):')
    if q=='+':
        x = float(input('first number'))
        y = float(input('second number'))
        c=x+y
        print('резы:'+str(c))

    elif q=='-':
        x = float(input('first number'))
        y = float(input('second number'))
        c=x-y
        print('резы:' + str(c))

    elif q=='^':
        x = float(input('first number'))
        y = float(input('second number'))
        c=math.pow(x,y)
        print('резы:' + str(c))

    elif q=='/':
        x = float(input('first number'))
        y = float(input('second number'))
        c=x/y
        print('резы:' + str(c))

    elif q=='log':
        while True:
            x = float(input('first number'))
            y = float(input('second number'))
            while x<=0 or y<=1:
                print('выберите верные аргументы')
                break
            while x>0 and y>0 and y!=1:
                c=math.log(x,y)
                print('резы:' + str(c))
                break
            break
    elif q=='up':
        x = float(input('first number'))
        y = float(input('second number'))
        c=round(x,int(input()))
        print('резы:' + str(c))

    elif q=='*':
        x = float(input('first number'))
        y = float(input('second number'))
        c=x*y
        print('резы:' + str(c))
    else:
        print(' Выберите предложенное действие')

