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