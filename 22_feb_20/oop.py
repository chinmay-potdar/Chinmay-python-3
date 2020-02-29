# Class : Machine in industry(Method and variables)
# Input:  Variable
# Method: function in class
# Object: Final product

#1. How to define class ?
# class keyword is used to write a class follwed by class name follwed by intendeation

# Syntax:
#class classname:
    #variable

    #method
#Example: (Follow naming convention)
    #rule:
    #1. Class name start with capital
    #2. method start with small
    
#class Student(object)
class Student:
    def _init_(self): # Init is constructor is special type of method to intialize Instance variable 
        self.id=1
        self.name="xyz" # Init is constructor is special type of method to intialize Instance variable 
    def disp(self):
        print(self.id,self.name)


# There are 3 type of variable in oops
# 1. Instance variable (Instance -- object)
# 2. Static variable 
# 3. Class Variable 
