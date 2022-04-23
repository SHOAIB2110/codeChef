class Property:
    def __init__(self,prop_type,prp_val,max_bid_price):
        self.prop_type=prop_type
        self.prp_val=prp_val
        self.max_bid_price=max_bid_price

class Tender:
    def ___init__(self,bname,prp_type,bid_price):
        self.bname=bname
        self.prp_type=prp_type
        self.bid_price=bid_price


if __name__=="__main__":
    n=int(input())    
    l=[]  
    l1=[]
    for i in range(n):
        prop_type=input()
        prp_value=int(input())
        m_b_p=int(input())
        l.append(Property(prop_type,prp_value,m_b_p))
    n1=int(input())
    for i in range(n1):
        bname=input()
        prp_type=input()
        bid_price=input()
        l1.append(Tender(bname,prp_type,bid_price))
