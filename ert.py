s=input().split()
a=list(map(int,s))
for i in range (len(a)):
    if a[i]==(a[i-1]+a[i-2]):
        print('Фибоначчи')
    else:
        print('Не фибоначчи')
