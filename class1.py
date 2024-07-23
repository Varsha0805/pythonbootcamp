class Student:
    def __init__(self,name,roll,branch,address,email):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.address=address
        self.email=email
    def __str__(self):
        return f'{self.name} {self.roll} {self.branch} {self.address} {self.email}'
s1=Student('varsha',62,"CSE","Hyd", "varsha@gmail.com")
print(s1)
