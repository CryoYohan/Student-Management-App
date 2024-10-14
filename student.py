'''
	Student class, extends from Person class
'''


class Student():
    def __init__(self,**args):
        self.idno = args.get('idno')
        self.lastname= args.get('lastname')
        self.firstname = args.get('firstname')
        self.course = args.get('course')
        self.level = args.get('level')
        
    def __str__(self)->dict: 
        #return f"{self.idno},{self.lastname},{self.firstname},{self.course},{self.level}"
        studenrecord = {
                'idno':self.idno,
                'lastname':self.lastname,
                'firstname':self.firstname,
                'course':self.course,
                'level':self.level
                }
        return studenrecord
        
    def __eq__(self,other)->bool: 
        if type(other) != type(self):                                       
            return False
        elif self.idno == other.idno:   
            return True
        else: 
            return False
        
    #user-defined modules
    #setters
    def setidno(self,idno:str)->None:       self.idno = idno
    def setcourse(self,course:str)->None:   self.course = course
    def setlevel(self,level:str)->None:     self.level = level
    #getters
    def getidno(self)->str:                 return self.idno
    def getlastname(self)->str:             return self.lastname
    def getfirstname(self)->str:            return self.firstname
    def getcourse(self)->str:               return self.course
    def getlevel(self)->str:                return self.level


