class Employee:
    def __init__(self,name,role,salary):# paramterized contructor
        self.name=name
        self.role=role
        self.__salary=salary #private data in encapsulation
    def get_salary(self):#public method with private data
        return self.__salary
    def Empdisplay(self):  #public method
        print(self.name,self.role)
class Company(Employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def Comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self):  #protected method
        print("Hiring for the manager role")
cobj=Company('Wipro','Gachibowli')
eobj=Employee('Varsha','developer',85000)
eobj.Empdisplay()
cobj._hiring()
