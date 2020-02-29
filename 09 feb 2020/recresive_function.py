# Function which call itself again and again is called recrusive function
 # There  must be a limit on call of function
 
 #syntax
 
n=4
def fact(n):
   if n==1:
       return 1
   else:
       return n*fact(n-1)
print(fact(4))

# Write a program to print sum of 10 naturnal number using recrussion.
