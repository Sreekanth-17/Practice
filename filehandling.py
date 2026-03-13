#Program that takes input from the user
age = int(input("Enter your age: "))
if age > 18:
    print("Eligible for voting card")

#program to create a txt file and write data
str = input("Enter a sentence: ")
f = open("data.txt", 'w')
f.write(str)
f.close()

#With statement (used where a pair of statements to be executed)
str = input("Enter a sentence: ")
with open("data.txt", 'a') as f:
    f.write(str + "\n")

#program to open stored text file
f=open("data.txt", 'r')
print(f.read())
f.close

f = open("hello.txt", mode = 'w')
if f:
    print("successfully opened")
print(type(f))

#Opens the file in read mode and stores all the data into the variable content
f = open("data.txt", 'r')
content = f.read(20)
print(type(content))
print(content)
f.close()

#Readline function
f = open("data.txt", 'r')
content = f.readline()
content1 = f.readline()
content2 = f.readline()
print(content)
print(content1)
print(content2)
f.close()

#close method
f = open("data.txt",'r')
if f:
    print("The exisiting file is opened successfully")
f.close()
