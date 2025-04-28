import sys
print(sys.version)
print("Anything you like")

myName = "Aishat"
print(myName) #This prints Aishat

# if 5 < 10:
print("10 is greater")
# or 
if 5 < 10:
    print("10 is greater")
x = str(3) #This is '3'
y = int(3) #This is 3
z = float(3) #This is 3.0

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

a, b, c = "Ofada Rice", "Stew", "Meat"
print(a, b, c)

d = e = f = "Olabisi"

print(d)
print(e)
print(f)

fruit = ["grape", "watermelon", "orange" ]
g, h, i = fruit

print(g)
print(h)
print(i)

l = "I "
m = "Love "
n = "Blue "

o = 5
p = 6
print(o+p)

print(l+m+n)

def myFunction():
    global t
    t = "Thanks"
    print(t)
myFunction()

def anotherFunction():
  print(t)
anotherFunction()
