class File:
    def __init__(self,path):
        self.path = path
        self.content = None
        self.nlines = None
        self.set_lines()
    def read(self):
        try:
            f = open(self.path,"r")
            self.content = f.read()
            f.close()
        except FileNotFoundError:
            print(f"file{self.path} not found! ")

    def readlines(self):
        try:
            f = open(self.path,"r")
            self.content = f.readlines()
            
            f.close()
        except FileNotFoundError:
            print(f"file{self.path} not found! ")
    
    def write(self,data):
            f = open(self.path, "w")
            f.write(data)
            f.close()
    def set_lines(self):
        try:
            f = open(self.path)
            content =f.readlines()
            self.nlines = len(content)
            f.close()    
        except:
            raise
    def show(self):
        if self.content!=None:
            print(self.content)
        elif self.content =="":
            print("File is empty")
        else:
            print("you need to read the file first")
        
