# class Painting:
#     def __init__(self,paintingID,painterName,paintingPrice,paintingtype):
#         self.paintingID=paintingID
#         self.painterName=painterName
#         self.paintingPrice=paintingPrice
#         self.paintingtype=paintingtype

# class ShowRoom:
#     def __init__(self,l):
#         self.l=l
#     def getTotalPaintingPrice(self,pt):
#         c=0
 
#     def getPainterWithMaxCountOfPaintings(self) :
#         nameCount = {}
#         rslt = []
 
#         for obj in self.plist :
#             if obj.pname in nameCount:
#                 nameCount[obj.pname] += 1
#             else :
#                 nameCount[obj.pname] = 1
 
#         # sort a dictionary based on values
#         # returns list of tuples of key,value
#         sort = sorted(nameCount.items(), key = lambda x : x[1])
 
#         # takes last tuple element 2nd value
#         val = sort[-1][1]
 
#         """
#         If more than one painter has highest
#         count of paintings, method returns that
#         name of the painter whose name comes first
#         as per the alphabetical orders(A-Z).
#         """
#         for value in sort :
#             if val == value[1]:
#                 rslt.append(value[0])
                 
#         if len(rslt) > 1 :
#             rslt.sort()
#             return rslt[0]
#         else :
#             return sort[-1][0]
                    


# n = int(input())
 
#     # take empty list
# plist = []

# # take values for particular object
# for val in range(n) :

#     # case insensitiveness consider
#     val1 = input().lower()
#     val2 = input().lower()
#     val3 = int(input())
#     val4 = input().lower()

#     # create a object with initial value
#     pobj = Painting(val1, val2, val3, val4)

#     plist.append(pobj)
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

s=sales.items()
for i in s:
    print(i[2])