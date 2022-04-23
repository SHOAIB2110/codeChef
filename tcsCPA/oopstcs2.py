"""Create a class Volca110 with below attributes
volcanoName :(string type)
county :(string type)
elevation :(number type)
arealnKtnSq :(number type)
last£ruptionYear :(number type)

Define the _1nit_ method which takes parameters in
above sequence and sets the values for
attributes volcanoName , COLJnty, elevation, arealnKmSq
and lastEruptionYear.
Create another class Eruption with attribute as below:
volcanolist a Ltst of Volcano Objects
fine ~ methods in this class as below:
canoBycountry: The method tak'es list of volcano
nd country as the argumenU3nd returns the list
gets whose country matches with the
a
Pl
5
Mauna Loa 
United States
4169
5271
1984

Mount Etna
Italy
3350
1190
2021

Mount Merapi
Indonesia
2930
1356
2020

Mount Vesuvius
Italy
1281
1232
1944

Mount Pinatubo
Philippine
1486
1486
1991

Italy
Mount Etna

"""
# import string


# class Volcano:
#     def __init__(self,volcanoName,country,elevation,areainkmsq,lasteruptionyear):
#         self.volcanoName=volcanoName
#         self.country=country
#         self.elevation=elevation
#         self.areainkmsq=areainkmsq
#         self.lasteruptionyear=lasteruptionyear
# class Eruption:
#     @classmethod
#     def findValconoByCountry(cls,vList,country):
#         x=[]
#         for i in vList:
#             if(i.country==country):
#                 x.append(i.country)
#         return x        
    
#     @classmethod
#     def isActive(cls,vList,Vname):
#         for i in vList:
#             if(i.volcanoName.lower()==Vname.lower()):
#                 if(2021-i.lasteruptionyear<25):
#                     return "HIGH PROBABILITY"
#                 if(2021-i.lasteruptionyear>25 and 2021-i.lasteruptionyear<50 ):
#                     return "LOW PROBABILITY"
#                 if(i.lasteruptionyear==2021):
#                     return "Active"
#                 else:
#                      return "Inactive"    
    



# n=int(input())
# objList=[]
# for i in range(n):
#     volcanoName=input()
#     country=input()
#     elevation=int(input())
#     areainkmsq=int(input())
#     lasteruptionyear=int(input())
#     objList.append(Volcano(volcanoName,country,elevation,areainkmsq,lasteruptionyear))
# cntName=input()
# valName=input()
# y=[]
# y=Eruption.findValconoByCountry(objList,cntName)
# if y:
#     print(*y)
# else:
#     print("No matches")    

# s=Eruption.isActive(objList,valName)
# print(s)

class volcano:
    def _init_(selddf,volcanoname,country,elevation,areainsqkm,lastyear):
        self.volcanoname=volcanoname
        self.country=country
        self.elevation=elevation
        self.areainsqkm=areainsqkm
        self.lastyear=lastyear
        
class eruption:
    def findvolcanobycountry(self,volcanolist,country):
        self.volcanolist=volcanolist
        self.country=country
        clist=[]
        for i in volcanolist:
            if i.country.upper()==country:
                clist.append(i)
        if len(clist):
            return clist
        return None
    def getvolcanocategorization(self,volcanolist,volcanoname):
        self.volcanolist=volcanolist
        self.volcanoname=volcanoname
        status=None
        currentyear=2021
        for i in volcanolist:
            lastyear=i.lastyear
            diff=currentyear-lastyear
            if i.volcanoname.upper()==volcanoname:
                status="active"
                return status
            elif diff<25:
                status="high probability"
                return "status"
            elif diff>=25 and diff<50:
                status="low probability"
                return status
            elif diff>50:
                status="inactive"
                return status
        return status
if __name__ == "_main_":
    n=int(input())
    volcanolist=[]
    for i in range(n):
        volcanonmae=input()
        country=input()
        elevation=float(input())
        areainsqkm=float(input())
        lastyear=int(input())
        obj1=volcano(volcanonmae,country,elevation,areainsqkm)
        volcanolist.append(obj1)
    searchname=input().upper()
    searchvolcano=input().upper()
    obj2=eruption()
    volcanolist.sort(key=lambda x:x.lastyear,reverse=true)
    clist=obj2.findvolcanobycountry(volcanolist,searchname)
    if clist is none:
        print("no matching records found.")
    else:
        for i in clis:
            print(i.volcnaoname)
            print(i.country)
            print(i.lastyear)
    status=obj2.getvolcanocategorization(volcanolist,search)
    if status is none:
        print("no volcano is available with the given name")
    else:
        print(status)