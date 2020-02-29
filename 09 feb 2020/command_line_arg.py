#command line Arg
#Run time is libary that support execution of program.

# Command Line: The argument which are given during run time.
'''
import sys  #(sys-System related packages)
sys.argv -> is string type array/list
argv is string array/list
sys.argv[0]-> #programnane
'''
import sys 
print(len(sys.argv))
print(sys.argv)

print(sys.argv[1:])
print(int(sys.argv[1])+int(sys.argv[2]))
