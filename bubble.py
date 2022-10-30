n=list(map(int,input().split()))
s=0
for j in range(len(n)):
    s+=1
    for i in range (len(n)-1):
        s+=1
        if n[i]>n[i+1]:
            n[i],n[i+1]=n[i+1],n[i]

print(n,s)
