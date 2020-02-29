z=open("ab.png","rb")
print(z.read())
w=open("f11.png","rb")
for i in z:
    w.write(i)
z.close()
