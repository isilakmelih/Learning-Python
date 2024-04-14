#coordinates = (1, 2)

#def gay_maker(isim, birth_place , year ):


#  print("anna\n" + isim + birth_place + str(year) )
#def cube(num):


#   return num*num*num


# anan = cube(10)

# male = True
# tall = True
#if male and tall:
#   print("anan1")
#elif male and not tall:
#   print("anan2")
#elif male or tall:
#   print(" anan3")
#else:
#   print("anan4")
#if and function
 #def numerator(num1, num2, num3):
#   if num1 >= num2 :
#      return "anan1"
  #  elif num1>= num2 and num2 >= num3 :
#     return "anan2"
  #  elif num1>= num2 or num1 >= num3 :
#     return "anan3"
   # else:
#     return "anan4"
# print( numerator(1,2,3))
#while
#i = 2
# while i<=5:
#   i= i+1
#  print(i)
#for loops,
# friends= ["ahmet","mehmet","çetin"]
# for index in range(5):
#   print(friends)
# def risetopower(inn, outtt):
 #    result = 1
  #   for index in range(outtt):
   #      result = result * inn
    # return result
# print(risetopower(2,3))
"""
listoflists = [
   [0,1,2],
   [3,4,5],
   [6,7,8],
]
anan=0
anan1=0
for index in listoflists:
   for aaa in index:
      print(aaa)
"""
#from typing import List

#try and except
"""   
try:
    aa = 10/0
    anan = int(input("integer"))
    print("number")
except ValueError as err:
    print(err)
except ZeroDivisionError as errr:
    print(errr)
"""
#openinfile
"""
sample = open("boş.txt", 'r+')
print(sample.readable())
sample.close()
"""
#using another page
"""
import scratch
print(scratch.)
"""
#class
"""
from scratch import teacher
teacher1 = teacher("anan", "anann", "physics", 2)
print(teacher1.name)

from chef import chef
class chinesechef(chef):
"""
#list example
"""
baban = "hello \t "

anan = "byby"
print("baban" + "anan")
message = 'One of Pythons strengths its diverse community.'

a=5
print("my fav number:",a)

guest = ["Einstein","Maxwell","newton"]
print(guest[0],"come to party")
print(guest[1],"come to party")
print(guest[2],"come to party")
print(guest,"newton deleted")
guest.remove("newton")
#del guest[0]
print(guest)
guest.insert(1,"dirac")
print(guest,"welcome")
print(guest[0],"come to party")
print(guest[1],"come to party")
print(guest[2],"come to party")
print(guest,"we have new guests")
guest.insert(3,"kopenhag")
guest.insert(4,"ahmet")
guest.append("ali")
guest.sort()
print(guest)
guest.reverse()
print(guest)
a = len(guest)
print(a)
#If an index error occurs and you can’t figure out how to resolve it, try printing your
#list or just printing the length of your list
"""
#list
"""
guest = ['Einstei','Maxwell','newton']
even_numbers = list(range(2,11,2))
even_numbers[0]=1
print(even_numbers)
b = [a**3 for a in range(1,11)]
print(b)
"""
#tuple
"""
dimension = (1,2,3)
print(dimension)
dimension = (2,3,4)
print(dimension)
"""
#else if
"""
names = ["a","b","c","d"]
names2 = ["a","c","f","g","h"]
for name in names2:
    if name.lower() in names:
        print("another name:")
    else:
        print("ok")

numbers =list(range(1,9))
for number in numbers:
    if number == 1:
        print("first")
    elif number == 2:
        print("second")
    elif number == 3:
        print("third")
    elif number == 4:
        print("fourth")
"""
#LİBRARY
"""
anans=[]
for anan in range(30):
    anan1 = {'name':'ali','lastname':'cinar'}
    anans.append(anan1)
print("{0}aaa".format(str(len(anans))))

cities = {
    'paris':{
        'population':'1M',
        'location':'france'
    },
    'konya':{
        'population':'1m',
        'location':'turkey'
    },
    'istanbul':{
        'population':'3M',
        'location':'turkey'
    }
}
for city,ity in cities.items():
    print("name of the city:",city)
    population_of_the_city =ity['population']
    location_of_the_cities = ity['location']
    print(population_of_the_city)
    print(location_of_the_cities)
"""
#input WHILE and some shit python take str value from input
"""
order_of_sandwiches = ['tuna','b','anan','tomato','anan','vegan','anan']
finished_ones = []
a=0
print("out of anan")
while 'anan' in order_of_sandwiches:
     order_of_sandwiches.remove('anan')
while a< len(order_of_sandwiches):
    finished_one=order_of_sandwiches[a]
    print("ready"+ order_of_sandwiches[a])
    finished_ones.append(finished_one)
    a+=1
"""
#FUNCTIONS
#When you use default values, any parameter with a default value needs to be listed
#after all the parameters that don’t have default values

"""
def make_album(artist, album):
    anan = {artist,album}
    return anan
input(make_album('tarkan','fındık'))
print(make_album())


def anan(nameeee):
    for ana in nameeee:
        n1 = ana
        print(n1)
names = ['babağ', 'babağ1', 'babağ2']
anan(names)
nw = []
def magician(aaa):
    print(aaa)
    while aaa:
       rand = aaa.pop() + '\t great'
       nw.append(rand)
    print(nw)
aa=['aaa1','aaa2','aaa3','aaa4']
magician(aa)

def build_profile(manufactur, model, **user_info):
 """"""
 anan = {}
 anan['manufacturer'] = manufactur
 anan['model'] = model
 for key , value in user_info.items():
     anan[key] = value
 return anan
user_profile = build_profile('subaru', 'ox',
location='princeton',
 field=True, anan = "aaa")
print(user_profile)
"""
#classes
"""
class restaurant():
    def __init__(self, names, type):
        self.names = names
        self.type = type
    def describe_restaurant(self):
        print("the type of restaurant is " + str(self.type) + ".")
        print("name:" + str(self.names)+ " .")
    def open_restaurant(self):
        print("openn")
my_restaurant = restaurant('ada','kkk')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
"""
