t=int(input())
for i in range(t):
    n=int(input())
    l1=list(map(int,input().split()))
    l1.sort()
    minSum=l1[0]+l1[1]
    print(minSum)
   
