# map function : Map is used to change or access all elements of sequence(list), s
#syntax:
list1=[1,2,3,4,5,6]
list0=[1,2,3,4,5,6]
#map(function_name, sequnce)
list2=list(map(lambda x:(x*x),list1))
print(list2)

list3=list(map(lambda x,y:(x*y),list1,list0))
print(list3)
