import math
sum = 0
n = int(input())
for i in range(int(n * math.log(n, 2))):
    sum += 1
print(sum)

