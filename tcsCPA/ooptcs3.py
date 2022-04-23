'''Create a class Traveler with below attributes
travelerName: (string type)
traveled Country: (list of string type represents the names of the country the traveler has travelled.
travelerAge: (nt type) countryFrom (string type)
Create a constructor which takes all the above attributes in the same sequence
Define another class Travel Agency with below attributes:
travelerlist: list of Traveler objects) Insight and having the below member functions:
countTravelers TraveledCountry: Which takes a string representing the name of a country as input, 
and returns the count of travelers from the travelerlist of TravelAgency who has travelled that country
TravelecTravelMaxCountry finds the traveler who has travelled highest number of countries
and turns the name of that traveler. If more than one such travelers are there having the highes'''
#import string


class Traveler:
    def __init__(self,travelerName,travelCountry,travelAge,countryFrom):
        self.travelerName=travelerName
        self.travelCountry=travelCountry
        self.travelAge=travelAge
        self.countryFrom=countryFrom

class TravelAgency:
    @classmethod
    def countTravelersTraveledCountry(cls,cnt_name,list_obj):
        cnt=0
        for i in list_obj:
            for j in i.travelCountry:
                if cnt_name==j:
                    cnt=cnt+1
        return cnt  
    @classmethod #define classmethod at every function declaration    
    def getTravelerTravelledMaxCountry(cls,list_obj):
        max=0
        
        for i in list_obj:
            if len(i.travelCountry)>max:
                name=i.travelerName
                max=len(i.travelCountry)
        return name        









n=int(input())
list_obj=[]
for i in range(n):
    travelerName=input()
    c=int(input())
    travelCountry=[]
    for j in range(c):
        travelCountry.append(input())
    travelerAge=int(input())    
    countryFrom=input()   
    list_obj.append(Traveler(travelerName,travelCountry,travelerAge,countryFrom)) 
cnt_name=input()       
c=TravelAgency.countTravelersTraveledCountry(cnt_name,list_obj) 
name=TravelAgency.getTravelerTravelledMaxCountry(list_obj)
print(c)
print(name)