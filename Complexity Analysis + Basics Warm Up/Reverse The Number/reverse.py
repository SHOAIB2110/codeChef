if __name__=='__main__':
    
    
    def Reverse_Integer(Number):
        Reverse =0
        while(Number > 0):
            Reminder = Number %10
            Reverse = (Reverse *10) + Reminder
            Number=(Number //10)
        return Reverse

    
    for i in range(int(input())):
        a=int(input())
        print(Reverse_Integer(a))
        
