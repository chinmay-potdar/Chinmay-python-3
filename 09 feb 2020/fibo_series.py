# fibo series
"""
variable=[]
variable=[i for i in range(10) i=i+(i-1)]
print(variable)
"""
t=[0,1]
i=0
for i in range(100):
    t[i]=t[i]+t[i+1]
    print(t[i])

