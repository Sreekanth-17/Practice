"""
# Writing of JSON data into a file function dump
import json    
student = {    
    "Name": "Peter",    
    "Roll-no": "0090014",    
    "Grade": "A",    
    "Age": 20,    
    "Subject": ["Computer Graphics", "Discrete Mathematics", "Data Structure"]    
}      
with open("data.json", "w") as write_file:    
    json.dump(student, write_file, indent=4)    

print(json.dumps(student, indent=4))    
"""

'''
# The function dumps()
import json 
student = {
    "Name": "Peter",
    "Roll no": "0090014",
    "Grade": "A",
    "Age" : 20
}
b = json.dumps(student)
print(b)
'''

"""
#serialization followed by deserialization
# tuple serialized to array and then deserialized to list
import json
a = (10,20,30,40,50,60,70)
print(type(a))
b = json.dumps(a)
print(type(json.loads(b)))
"""

'''
#the load() method
import json  
student  = {    
"Name" : "Peter",    
"Roll-no" : "0090014",    
"Grade" : "A",    
"Age": 20,    
}    
    
with open("data.json","w") as write_file:    
    json.dump(student,write_file)    
    
with open("data.json", "r") as read_file:    
    b = json.load(read_file)    
print(b)  
'''