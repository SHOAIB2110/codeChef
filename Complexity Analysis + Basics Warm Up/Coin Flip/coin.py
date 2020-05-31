# cook your dish here
t=int(input())
for i in range(t):
    g=int(input())
    for i in range(g):
        i,n,q=list(map(int,input().split()))
        if (i==1  and q==1) or (i==2 and q==2 ):
            if(n%2==1):
                print(n//2)
            else:
                print(n//2)
                
        else:
            if(n%2==1):
                print(n//2+1)
            else:
                print(n//2)
