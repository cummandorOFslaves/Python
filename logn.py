import math
n = int(input())
sum = 0
for i  in range(int(math.log(n, 2))):
    sum += 1
print(sum)