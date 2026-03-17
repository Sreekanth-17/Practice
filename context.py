
class context_manager():    
    def __init__(self):    
        print ("The 'init' method is called")              
    def __enter__(self):    
        print ("The 'enter' method is called")    
        return self          
    def __exit__(self, exc_type, exc_value, exc_traceback):    
        print ("The 'exit' method is called")    
with context_manager() as manager:    
    print ("The 'with' statement is a block") 


class file_manager():    
    def __init__(self, file_name, mode):    
        self.filename = file_name    
        self.mode = mode    
        self.file = None              
    def __enter__(self):    
        self.file = open(self.filename, self.mode)    
        return self.file          
    def __exit__(self, exc_type, exc_value, exc_traceback):    
        self.file.close()      
# At last, load the file     
with file_manager('test_file.txt', 'w') as file:    
    file.write("True")      
print (file.closed)    



from pymongo import MongoClient as moc  
class mongo_db_connection_manager():  
    def __init__(self, host_name, port = '27017'):  
        self.hostname = host_name  
        self.port = port  
        self.connection = None   
    def __enter__(self):  
        self.connection = moc(self.hostname, self.port)  
        return self    
    def __exit__(self, exc_type, exc_value, exc_traceback):  
        self.connection.close()   
# Now, connect with a localhost  
with mongo_db_connection_manager('localhost', 27017) as mongo:  
    collection_1 = mongo.connection.SampleDb.test  
    data_1 = collection_1.find_one({'_id': 142})  
    print (data_1.get("name"))  