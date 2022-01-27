#default
from unicodedata import name


def sum(number):
    res = 0
    for e in number:
        res += e  
    return res

number = [1, 2, 3, 4]

print(sum(number))
# args
def sum(*numbers):
    res = 0
    print(numbers)
    print(type(numbers))
    for e in numbers:
        res += e  
    return res

print(sum(1,2,3,4,5))

# Kwargs
def students(**kwargs):
    for v in kwargs.values():
        print(v)
    

students(name="Jake",student_number = "401")

def students(**students):
    print(students)
    for v in students:
        print(v)

students(name="Jake",student_number = "401")

# args&Kwargs

def weird(*args, **kwargs):
    res = 0
    for e in args:
        res += e 
    
    for k,v in kwargs.items():
        print(k,":",v)

    return res

weird(1, 2, 3, name="jake", student_number = 401)

# Unpacking

l1 = [1,2,3,4]
l2 = [1,2]
merged_l = [*l1,*l2]
print(merged_l)

d1 = {"name" : "jake" , "number" : 402}
d3 = {"name" : "sky" , "grade" : 74}

d_merged_3 = {**d1,**d3}
print(d_merged_3)