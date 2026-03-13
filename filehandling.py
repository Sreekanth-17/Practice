"""

age = int(input("Enter your age: "))
if age > 18:
    print("Eligible for voting card")

"""
'''
age = input("Enter your age: ")
f = open("data.txt", 'w')
f.write(age)
f.close()
'''

"""
f=open("data.txt", 'r')
print(f.read())
f.close
"""  

f = open("hello.txt", mode = 'w')
if f:
    print("successfully opened")
print(type(f))
