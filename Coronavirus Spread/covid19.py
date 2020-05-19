t=int(input())

list1=[]

for i in range(t):
    man=[]
    infected=1
    in1=int(input())
    list1=list(map(int,input().split()))

    for j in range(in1-1):
        if list1[j+1]-list1[j]<=2:
            infected+=1
        else:
            man.append(infected)
            infected=1
    man.append(infected)
    print(min(man),max(man))
