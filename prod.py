import timeit
print('введите матрицу 3х3 для возведения в степень -1')
a1,a2,a3=map(int,input().split())
a4,a5,a6=map(int,input().split())
a7,a8,a9=map(int,input().split())

det=a1*a5*a9+a8*a3*a4+a7*a2*a6-a7*a5*a3-a1*a6*a8-a9*a4*a2
det1=1*(a5*a9-a8*a6)/det
det2=-1*(a4*a9-a7*a6)/det
det3=1*(a4*a8-a7*a5)/det
det4=-1*(a2*a9-a8*a3)/det
det5=1*(a1*a9-a7*a3)/det
det6=-1*(a1*a8-a7*a2)/det
det7=(a2*a6-a5*a3)/det
det8=-(a1*a6-a4*a3)/det
det9=(a1*a5-a4*a2)/det

print('результат в виде обратной матрицы:')
print((det1,' ',det4,' ',det7))
print(det2,' ',det5,' ',det8)
print(det3,' ',det6,' ',det9)

print(timeit.timeit())