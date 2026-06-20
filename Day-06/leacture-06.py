#Today we learn about the function in python 
"""
what is function 

block of statement  that perform a specific task

imp point of fuction 

function hava two main type 

1 simple type fuction means that not return any value just we creating and use it manay time

2 is return type fuction that take perameter and argument and retun us some value after processing

funtion sytex is

def => means defination
fuction name def dislay
arguments ie  like(a,b)
some work
return type 

def dispalyinfo() :
print("faizan",25,Software engineer)

how to use just write
displayinfo()

another type is retune ie

def sun(paramenter1, parameter2):
s=p1+p2
return s

print(sum(1,2))

this is basice cocept of funtion


"""


#lets Do some practice question

#WAP that take two number form user and print average of 3 number 
#same as for the print avarge of student number
"""
def average_of_3no(a, b, c):
    
    result = (a + b + c) / 3
    return result

x = int(input("Enter 1st number = "))
y = int(input("Enter 2nd number = "))
z = int(input("Enter 3rd number = "))

print("average is", average_of_3no(x, y, z))

#Q2

def marks_of_student(a, b, c):
    result = a + b + c
    print("marks_of_student is:", result)


x = int(input("Enter 1st number = "))
y = int(input("Enter 2nd number = "))
z = int(input("Enter 3rd number = "))

marks_of_student(x, y, z)

"""

# In python we have  two main type funtions 

#One is built in fuction

#2nd is user defined Function

"""
built in         user define functions are the 
print()         what we create by ownwish or ownneed
len()          display()
type()         sum()
range()        add()



#WAF to print lenth of a list (list is the pramter) 

name = ["ali", "faizan", "shah", "abbas", "hussain", "ali"]
my_list = ["ali", "faizan", "shah", "abbas", "hussain", "ali"]

def print_length(target_list):
    print(len(target_list))

def print_elements(target_list):
    for item in target_list:
        print(item, end=" ")

print_length(name)
print_length(my_list) 

print_elements(name)
print() 
print_elements(my_list) 



#WAP to find the factorail of n (n is the parameter)


def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

cal_fact(5)

#WAP to convert USD in pkr
def converter(dollar, pkr_rate):
    total_pkr = dollar * pkr_rate
    return total_pkr

# Input
usd = int(input("Enter USD: "))
rate = int(input("Enter current PKR rate: "))

# Function Call & Print
result = converter(usd, rate)
print("Total PKR:", result)




"""

#own logic of funtion

def convert(usd_val):
    pkr_val =usd_val*180
    print(usd_val,"pkr =",pkr_val,"pkr")

a=int(input("Enter USD"))

convert(a)


