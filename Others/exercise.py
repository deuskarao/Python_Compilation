import matplotlib.pyplot as matplot #analiz tablosu cıkartır

my_list = [1, 2, 3]

my_list[2] = 6

my_list.append(31)

my_list.reverse()

my_list.pop()

print(my_list)

my_alphabet = list([chr(value) for value in range(97, 123)])

my_string = "abc"

my_string = my_string.upper()
print(my_string)


mylist = [1, 2, 3, ["a", "b"]]

mylist.append(["x", 7])

print(mylist)


dictionary1 = {"x" : "y", "a" : 100, "v" : {"x" : "y"}}

dictionary1["v"]["x"] = "tt"

dictionary1["nq"] = "sas"

dictionary1["nr"] = {"e":"g"}

dictionary1["list"] = (1,2,3)

print(dictionary1)


my_list_set = (1,2,3,1,2,3,4,5,4,5)

myset = set(my_list_set)

print(myset)

myset2 = set()

myset2.add(1)

myset2.add(2)

print(myset2)


#tuple is unchangable ##immutability

my_tuple = ("a", 31, "c")

#my_tuple[1] = 2  (when you don't want the code to be changed then use tuple instead of list)

print(my_tuple)



my_dictionary = {"k1":2, "kk":[4,{"kkkk":"b"}]}

print(my_dictionary["kk"][1]["kkkk"])

print("------")

x = 31

y = 62

a = x != y

b = x > y

c = x >= 10.123

print(a)
print(b)
print(c)

print("------")

#and or not

k = 1
l = 2
m = 3
n = 3

t = k > l and m > l

f = k > l or m > l

i = not m == n

print(t)
print(f)
print(i)

print("------")

#if - else


list1 = ("a", "b", "c")
list2 = ("x", "y", "t")

letter = input("Enter a character: ")

if letter in list1:
    print("Letter is unacceptable")
elif letter in list2:
    print("Letter accepted")
else:
    print("Try another letter")


print("------")


x = int(input("Enter first number: "))

y = int(input("Enter second number: "))

if x > y:
    print(f"x is greater ----->  {x} > {y}")
elif x == y:
    print(f"x is equal y ----->  {x} = {y}")
else:
    print(f"y is greater ----->  {y} > {x}")

print("------")


new_list = [("a","b"), ("c", "d"), ("e", "f")]
for (x,y) in new_list:
    print(x)
    print(y)

print("------")


new_list1 = [("1","2", "3"), ("4", "5", "6"), ("7", "8", "9")]
for (x,y,z) in new_list1:
    print(z)

print("------")


new_dictionary = {"k1" : "x", "k2" : "y", "k3": "z"}
for (key,value) in new_dictionary.items(): #parantez olmadan da calısır key,value ya da (key,value)
    print(key)
    print(value)

print("------")


list1 = [10, 20, 30, 40, 50]

for element in list1:
    if element == 40:
        break
    print(element*10)

print("------")


for element in list1:
    if element == 20:
        continue
    print(element)

print("------")

x = 0

while x <= 5:
    print("NİGGA")
    x = x + 1

print("------")

list3 = [1,2,3,4,5,6]

while 3 in list3:
    print("Still in")
    list3.pop()

print("------")

p = 0
while p < 10:
    # print("value p: " + str(p)) slttakiyle aynı çıktıyı verir
    print(f"value p: {p}")
    p += 1

print("------")


o = list(range(5,20))
print(o)
print("------")

for num in list(range(5,21,3)):
    print(num)

print("------")

#ENUMERATE

for item in enumerate(list(range(5,20))):
    print(item)

print("------")

import random

list99 = (list(range(0,20)))

random.shuffle(list99)

print(list99)

print("------")

## ZİP

sport_list = ["run","swim","basketball"]

calories_list = [100,200,300]

day_list = ["monday","tuesday","wednesday"]

new_list = list(zip(sport_list,calories_list,day_list))

print(new_list)

print("------")

list100 = [item*10 for item in list(range(10,31))]

print(list100)

print("------")

def my_func(*args):
    return (args)

print(my_func(1,2,3,4,5,6))

print("------")

def func_2(**kwargs):
    return (kwargs)

print(func_2(a=100,b=200,c=300))

print("------")

def divide(number):
    return number / 2

print(divide(30))

print("------")

list_n = [10,20,30,40,50]

print(list(map(divide,list_n)))
# (list(map ... seklinde yazmadan sadece kaydettigi konumu gosterir map

print("------")

#list(filter ile buyuk dosyalarda koşula uyanları getir diyerek kolaylık saglayabıliriz
def control_s(string):
    return "john" in string

fighter_list = ["conor", "khabib", "john", "john jones", "John", "Conor", "Khabib"]

print(list(filter(control_s,fighter_list)))

print("------")

#lambda

list5 = [1,2,3,4]
multi = list(map(lambda number:number*5, list5))

print(multi)

print("------")

#DECORATOR

def decorator_function1(func):
    def wrapper_function1():
        print ("wrapper started" )
        func ()
        print ("wrapper stopped" )
    return wrapper_function1

def func_new1():
    print ("hello world")

example_func = decorator_function1(func_new1)

print(example_func())

print("------")  #ustteki ile alttaki aynı sonucu verecek

#@decorator_function
def func_new():
    print ("fuck bitches")

print(func_new())

print("------")

# snake = my_list
# camel = myList

class Musician():
    def __init__(self, name, age, instrument):
        self.name = name
        self.age = age
        self.instrument = instrument

    def sing(self): #Method
        print(f" {self.name} is the god of {self.instrument}")


musician = Musician("Defkhan", 45, "Lyrics", )


print(f""" 
{musician.name}
{musician.age}
{musician.instrument}
""")

print(musician.sing()) #without () it would just bring where the file is saved

print("------")

class DogYears():
        year_factor = 7

        def __init__(self, age=5): #age = 5 default degeridir istendigi zaman deger atanabılır parantez içinde
            self.age = age
            self.age_multiplied = age * 7
        # alttaki gibi ayrıca ugrasmadan veya self yanına multiplied seklinde deger vermeden de boyle eklenebilir

        def calculation(self):
            return self.age * self.year_factor
               #self.year veya DogYears.year_factor seklinde 2 ayrı yazımla gorulebılır


dawg = DogYears()

print(dawg.age_multiplied)
print(dawg.calculation())

print("------")

##INHERİTANCE
class Class1():
    def __init__(self):
        print("Class 1 created")
    def method_1 (self):
        print ("method 1")
    def method_2(self):
        print ("method 2")


inherit1 = Class1()

print(inherit1.__init__())

print("------")

class Class2(Class1):
    def __init__(self):
        Class1.__init__(self)
        print("Class 2 created")


inherit2 = Class2()

print(inherit2.__init__())

print("------")

##POLYMORPHİSM

class Apple():
    def __init__(self, name):
        self.name = name
    def information (self):
        return self.name + " 100 calories"


class Banana():
    def __init__(self, name):
        self.name = name
    def information (self):
        return self.name + " 200 calories"


banana = Banana("banana")

apple = Apple("apple")

info_list = [banana, apple]

for fruit in info_list:
    print(fruit.information())

print("------")

def get_info(fruit):
    print(fruit.information)

print(f"{get_info(banana)}" + f"\n{get_info(apple)}")

print("------")


#Special Methods

class Fruits_1():
    def __init__(self,name,calories):
        self.name = name
        self.calories = calories

    def __str__(self):
        return f"{self.name}" " ----> " f"{self.calories} calories"

fruitstr = Fruits_1("Orange", 131)

print(fruitstr)

print("------")

## search for more python special methods


#ERROR HANDLING

while True:
    try:
        my_int = int(input("Enter a number: "))
    except:
        print ("Enter a number!!!")
        continue
    else:
        print("     Passed")
        break

print("---------")
print("-------------")

#print("---------")

# alttakı farklı dosyalarla calısmayı saglayan kod yazılan vırusun oldugu klasorde farklı dosyaları .txtleri dahil edebiliriz

# mode a = append -- r = read -- w = write

#with open("myfile.txt" ,mode="a" ) as my_new_file_3:
#   my_new_file_3 write(" test 5")

print("-------------")


while True:
    try:
        num = float(input("Deposit: "))
        break
    except ValueError:
        print("!!!")


nums = range(1, 1000)

print("-------------")


def calculate_factorial():
    n = 5
    start = 1

    for i in range(1, n + 1):
        start = start * i

    print(start)


calculate_factorial()

print("-------------")