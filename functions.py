"""
#function with return statement
def get_greeting():
    msg = ("Hello from a function")
    return msg
print(get_greeting())

#arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(name): #name is a parameter
    print("Hello", name)
my_function("Emil")# Emil is an argument

#number of arguments must be correct
def my_function(fname, lname):
    print(fname + ' '+ lname)
my_function("Emil", "Refsnes")

#default value parameters
def my_function(name= "friend"):
    print("Hello", name)
my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#keyword argument
def my_function(animal, name):
    print("I have a",animal)
    print("My",animal+"'s name is",name)
my_function(animal="dog", name="Buddy")

#mixing keyword and positional arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

#*args
def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:",args[1])
    print("Third argument:",args[2])
    print("All arguments:", args)

my_function("Emil","Tobias","Linus")

# regular parameters with *args
def my_function(greeting, *names):
    for name in names:
        print(greeting,name)
my_function("Hello", "Emil", "Tobias", "Linus")

#a function that calculates the sum of any number of values
def my_function(*numbers):
    total = 0
    for num in numbers:
        total+=num
    return total
print(my_function(1,2,3))
print(my_function(10,20,30,40))
print(my_function(5))

#finding the maximum value
def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num>max_num:
            max_num = num
    return max_num
print(my_function(3,7,85,869,95,334,8887,9620,7496,33147,8596,35874,852156))

#**kwargs
def my_function(**myvar):
    print('Type:',type(myvar))
    print('Name:',myvar["name"])
    print('Age:', myvar["age"])
    print('City:', myvar["City"])
    print('All data:',myvar)
my_function(name="Tobias", age = 30, City = "Bergen")

def my_function(title, *args, **kwargs):
    print("Title:",title)
    print("Positional arguments",args)
    print("Keyword arguments",kwargs)
my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

#unpacking a list using *
def my_function(a,b,c):
    return a+b+c
numbers = [12,25,84]
result = my_function(*numbers)
print(result)
"""
#unpacking a dictionary using **