"""Create class Medicine with below attributes: MedicineName - String batch - String disease - String price - int

Create class Solution and implement static method "getPriceByDisease" in the Solution class. This method will take 
array of Medicine objects and a disease String as parameters. And will return another sorted array of Integer objects
 where the disease String matches with the original array of Medicine object's disease attribute (case insensitive search).

Write necessary getters and setters.

Before calling "getPriceByDisease" method in the main method, read values for four Medicine
 objects referring the attributes in above sequence along with a String disease. Then call the
  "getPriceByDisease" method and print the result."""

class Medicine:
    def __init__(self,MedicineName,batch,disease,price):
        self.MedicineName=MedicineName
        self.batch=batch
        self.disease=disease
        self.price=price  
    
class Solution:
    @classmethod
    def getPriceByDisease(cls,objectList,dis):
        res=[]
        for i in objectList:#here i is object 
            if(i.disease.lower()==dis.lower()):
                res.append(i.price)
        return res        






n=int(input())
objectList=[]
for i in range(n):
    MedicineName=input()
    batch=input()
    disease=input()
    price=int(input())

    #u can create class object-Medicine(MedicineName,batch,disease,price)
    #here if you want to take class object into list you can use the following method]
    
    objectList.append(Medicine(MedicineName,batch,disease,price))
dis=input()
x=[]
x=Solution.getPriceByDisease(objectList,dis)
print(x)
