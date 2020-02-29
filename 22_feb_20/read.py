# File handling in python
# Syntax
# 1. open()
f=open('a.txt')
print(f.read)
print(f.read(8))
print(f.readline())

#readline function is used to read single line in file.

for line in f:
    print(line)
f.close()
