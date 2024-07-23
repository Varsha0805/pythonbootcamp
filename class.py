class Student:
    #static data
    branch="CSE"
    def __init__(self,name,roll,address,email):
        self.name=name
        self.roll=roll
       #self.branch=branch
        self.address=address
        self.email=email
    def display(self):
        print("Name is:",self.name)
        print("Roll is:",self.roll)
        print("Branch is:",self.branch)
        print("Address is:",self.address)
        print("Email is:",self.email)
s1=Student('varsha',62,"Hyd","varsha@gmail.com")
s1.display()
