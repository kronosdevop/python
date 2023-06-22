ford = ("ram","bronco","raptor","endeavour","mustang")
print(ford)

##########################################

car1 = ("audi","bmw","mercedes")
car2 = ("jeep","ford","chevrolet")
car3 = ("tata","maruthi","toyota")
print(car1,car2,car3)


#############################################################################

x=12
y=45.6786666
z= 24j
print(type(x))
print(type(y))
print(type(z))


#############################################################################

delf = "ronin"
selg = ""
print (bool(selg))
##############################################################################

a=2333
b=400
if (a>b):
    print("a is greater than b")
else:
    print("b is greater than a")

##############################################################################

x = 10
print(x)

x /- 10
print(x)

x += 10
print(x)

x -= 10
print(x)

x *= 10
print(x)

##################################################################################

print(10==20)
print(10>20)
print(10<20)
print(10>=20)
print(10<=20)
print(10<20)

##################################################################################

string = "abcdefghijlmno"

print(string[3:7])
print(string[:-3])

print(string.replace('f','z'))

####################################################################################

#ford = "ram","bronco","raptor","endeavour","mustang"
#print(type(ford[0:4]))
####################################################################################

knife = [36,47,56,63,72]
knife.append(9999)
knife.append(555)
knife.append(666)
print(knife)
####################################################################################
mixed = [1,2,'a',['d','f'],(44,55,66,77)]
print(mixed[3])

######################################################################################
#salaries = {"john":36,"jumbo":47,"kidd":56,"zoro":63,"brooke":72}
#print(type(salaries["brooke"]))
######################################################################################
salaries = {"john":36,"jumbo":47,"kidd":56,"zoro":63,"brooke":72}
print(salaries.get("zoro"))
######################################################################################
sal = {"ichigo": 34,"kenpachi":56,"biyakuya":65}
print(sal)
sal["madarame"]=27
print(sal)
del sal["madarame"]
print(sal)


for key,val in sal.items():
    print(key,val)

print("madarame" in sal)    
######################################################################################
listnew = []
for x in range (0,10):
    listnew.append(x)
#print(listnew)
######################################################################################
l = [x for x in  range (0,9)]
s = {x for x in  range (0,9)}
t = tuple(x for x in  range (0,9))
d = {x: x*x  for x in  range (0,9)}
print(l)
print(s)
print(t)
print(d)
######################################################################################
x=15
if x<20:
   print("x is less than 20")
   if x<15:
       print("x is less than 15")
elif x==20:
    print("x is equal to 20")
else:
    print("x is greater than 20")
######################################################################################
num1 = [x for x in range (0,20)]

for x in num1:
    if x==(15): continue
    print(x,end= ", ")


print("done")
######################################################################################
x = 100

while x != 0:
    #print(x)
    x -= 10

######################################################################################
r =lambda x, y : x*y
r (2,3)
print(r(2,3))



def multiply (x,y):
   return x * y
print(multiply(3,5))
print(multiply(2,34))
######################################################################################
def downloadfile(url):
    print("establish connection" + url)
    print("open connection" + url)
    print("downlaod data")
    print("log into DB" + url)
    print("close connection" + url + "\n\n")

downloadfile(" //https:www.diablo.in ")
downloadfile(" //https:www.draken.in ")
downloadfile(" //https:www.everglade.in ")
downloadfile(" //https:www.ronsonorg.in ")
downloadfile(" //https:www.fellerock.in ")
downloadfile(" //https:www.smithson.in ")
######################################################################################

def createmultiplier(x):
    return lambda y : x * y

multiply = createmultiplier(10)

def execute(f , arg):
    return f(arg)

print(execute(multiply , 15))
print(execute(multiply , 25))

######################################################################################

bleach = ["ichigo","chad","uriyu","chad","cone","rukiya","urahara","yorichi"]
print(bleach[4])
print(len(bleach))


bleach[4] = "biyakuya"
print(bleach[4])


for x in bleach:
    print(x)

bleach.append("karuzou")
print(len(bleach))
print(bleach)

bleach.pop(0)
print(bleach)

bleach.remove("urahara")
print(bleach)