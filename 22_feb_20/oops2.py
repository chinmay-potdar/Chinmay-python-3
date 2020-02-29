# How to create object ?
#Syntax:
#Object =classname
# When we create object, construct will get call,
#Example


class Student:
    """Doc String-->Documentation"""
    def __init__(self,a,b): # Init is constructor is special type of method to intialize Instance variable
        self.id=a
        self.name=b # Init is constructor is special type of method to intialize Instance variable 
    def disp(self):
        print(self.id,self.name)
s1=Student(1,"Amit")
s1.disp()
s2=Student(2,"Ajay")
s2.disp()
print(Student.__doc__)


# If we create object in class, the memory will allocated in object and all instance variables and methods will be intialize
