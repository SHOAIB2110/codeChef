# cook your dish here
if __name__=='__main__':
    for i in range(int(input())):
        s=input()
        l=len(s)
        s1=s[:int(l/2)]
        if l%2==0:
            s2=s[int(l/2):]
        else:
            s2=s[int(l/2)+1:]
        s1=sorted(s1)
        s2=sorted(s2)
        if s1==s2:
            print("YES")
        else:
            print("NO")
