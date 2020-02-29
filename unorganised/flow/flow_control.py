#cd /home/chinmay/Public/programs/Session
''' To control flow of data we have flow control statement
    1. Decision make statement
        Type of decision make statement 
        1. if 
        Syntax:
            if condition:
                statement
            '''
        #Example :
a=True
if a:
    print("Now time to leave")
'''  
        2. if..else
         Syntax:
         if condition:
            statement
        else:
            statement
'''
#Example

a=5
if a%2==0:
    print("Even")
else:
    print("odd")
'''
    
        
        3. if...elif (Nested else if)
        Syntax: 
        if condition:
            statement
        elif condition:
            statement
        elif condition:
            statement
        elif condition:
            statement
        elif condition:
            statement
        else: 
            statement
'''
#Example

a=80
if a>=75:
     print("Distinction")
elif a>=60:
    print("First")
elif a>=50:
    print("second")
elif a>=40:
    print("pass")
else:
    print("fail")

# Problem statement
'''
Q1. 

Units       Bill
----------------------------
0 -50       unit * 0.5
51 -100     unit * 0.75
101-200     unit * 0.95+1
201-above   unit * 0.99 +5

Q2. If customer wants to buy keyboard mouse and minitor
then vendor will give discount according to following condition
1. if qty of keyboard is greater than 100, tten 25% discount on total price.
2. if qty of mouse is greater than 200, then 50% discount.
3. if qty of minitor is greater then 200, then 10% discount will be given.
'''
