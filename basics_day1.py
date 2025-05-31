# 1. Variables and Data Types
name = "Sakshi"
age = 21
is_ready = True
print("Name :",name)
print("Age :",age)
print("Ready to learn?",is_ready)

# 2. Lists, Tuples, Sets, Dictionaries
my_list=[1,2,3,4]
my_tuple = ("apple","mango")
my_set = {1,2,2,4}
my_dict={"name":"sakshi","field":"IT"}
print("List :",my_list)
print("Tuple :",my_tuple)
print("Set :",my_set)
print("Dictionary :",my_dict["field"])

# 3. If-Else
score = 80
if score>=60:
    print("Result : Pass")
else:
    print("Result : Fail")
    
# 4. Loops
for fruit in["apple","mango","cherry"]:
    print("Fruit :",fruit)

# 5. Functions
def square(n):
    return n*n
print("Square of 5 :",square(5))