#обратная матрица
import numpy as np
import timeit
a1, a2, a3 = map(int, input().split())
a4, a5, a6 = map(int, input().split())
a7, a8, a9 = map(int, input().split())

a = np.array([[a1, a2,a3], [a4,a5,a6],[a7,a8,a9]])
b = np.linalg.inv(a)

print ("Обратная матрица к A:\n", b)
print(timeit.timeit())