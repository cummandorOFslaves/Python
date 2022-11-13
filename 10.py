import modr
import timeit


a=list(map(int,input().split()))

n = input('Для сортировки методом "быстрая сортировка", нажмите 1. Для сортировки методом "рассческа", нажмите 2: ')
if n == 1:
    print(modr.sr(a))

else:
    print(modr.rs(a))

print(timeit.timeit())