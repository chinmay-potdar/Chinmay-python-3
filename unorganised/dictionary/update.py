# The update function in dictionary has booth function of upadate and insert
# The update first look if keys is available, if its available then it update the existing keys
# If key is not available then it create the new key.
my_dict={
    "name":"chinmay",
    39:"This is the float",
    "age":20,
    "location":"mumbai"
        
             }
print(my_dict.update({"name":"sumit"}))
print(my_dict)

print(my_dict.update({"college":"vjti"}))
print(my_dict)

