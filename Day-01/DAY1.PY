print(" hellow my name faizan ahamad")
print("I'm from gilgit and current doing software engineering")

name ="faizan"
Age= 25
print(name)
print(Age)
print(type(name))
print(type(Age))
#know the find the sum and difference of two numbers
num1= 10
num2= 5
sum= num1 + num2
difference= num1 - num2
print("the sum of", num1, "and", num2, "is", sum)
print("the difference of", num1, "and", num2, "is", difference)
#know the find the area of a circle
radius= 7
pi= 3.14    
area= pi * radius ** 2
print("the area of the circle with radius", radius, "is", area)



"""
type of Operators in python
 

logical operators: and, or, not
Assignment operators: =, +=, -=, *=, /=, %=, **=, //=

""" 
#use of the operators

#1. Arithmetic Operators
#1. Arithmetic Operators: +, -, *, /, %, **, // 
a= 10
b=20
c= a + b
d= a - b
e= a * b
f= a / b
g= a % b #modulus means to find the remainder of a division
h= a ** 2  #exponentiation means to find the power of a number
i= a // 3  #floor division means to find the quotient of a division and round it down to the nearest integer
print("the sum of a and b is", c)
print("the difference of a and b is", d)
print("the product of a and b is", e)                   
print("the division of a and b is", f)
print("the modulus of a and b is", g)
print("the exponent of a is", h)
print("the floor division of a by 3 is", i)
 

 #know Assignment operators
 # Assigmanment opertors give a value to a variable also tell us that the vslue is ture and fasle.
 #relational operators: ==, !=, >, <, >=, <=.
x= 5
y=10
print("the value of x is", x)
print("the value of y is", y)
print("x is equal to y:", x == y)
print("x is not equal to y:", x != y)
print("x is greater than y:", x > y)  
print("x is less than y:", x < y)
print("x is greater than or equal to y:", x >= y)
print("x is less than or equal to y:", x <= y)

#know we learn logical operators

#logical operators: and, or, not

# (And) means both conditions must be true, or means at least one condition must be true, not means to reverse the logical state of a condition.
 
#(not) is used to reverse the logical state of a condition. If a condition is true, not will make it false, and if a condition is false, not will make it true.
#or is used to combine two conditions. If at least one of the conditions is true, the result will be true. If both conditions are false, the result will be false.


a= True
b= False
print("a is True:", a)
print("b is False:", b)
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)
print("not b:", not b) 

#know we learn Assignment operators
# Assignment operators: =, +=, -=, *=, /=, %=, **=, //=
x= 5
y= 10    
print("the value of x is", x)
print("the value of y is", y)

print(a==b)#false
print(a!=b)#true
print(a >= b)#true
print(a <= b)#false
print(a > b)#true
print(a < b)#true

#also we can use like that

x += 5  #x= x + 5
print("the value of x after adding 5 is", x)
x -= 2  #x= x - 2
print("the value of x after subtracting 2 is", x)
x *= 3  #x= x * 3
print("the value of x after multiplying by 3 is", x)
x /= 4  #x= x / 4
print("the value of x after dividing by 4 is", x)
x %= 3  #x= x % 3
print("the value of x after modulus by 3 is", x)
x **= 2  #x= x ** 2
print("the value of x after exponentiation by 2 is", x)
x //= 2  #x= x // 2
print("the value of x after floor division by 2 is", x)


# know we learn about type conversion
# type conversion is the process of converting one data type to another data type.
# there are two types of type conversion: implicit and explicit.            
# implicit type conversion is the process of converting one data type to another data type without the programmer's intervention. It is also known as type coercion.
# explicit type conversion is the process of converting one data type to another data type with the programmer's intervention. It is also known as type casting.

# this is the type of implicit type conversion where python automatically converts the data type of a variable to another data type when it is necessary.
x= 5
y= 2.5
z= x + y
print("the value of z is", z)
# this is the examplr of implicit type conversion where python automatically converts the data type of a variable to another data type when it is necessary.

#where as we can also do explicit type conversion where we can convert one data type to another data type with the programmer's intervention.
 
 # know we learn about type casting
# type casting is the process of converting one data type to another data type with the programmer's intervention. It is also known as type conversion.
# there are three built-in functions for type casting: int(), float(), and str(). for expalmple, we can use int() to convert a float to an integer, float() to convert an integer to a float, and str() to convert a number to a string.
x=2
y=3.5
z= str(x) + str(y)
print("the value of z is", z)

#anothr example of type casting
a= 10
b= 2.5
c= int(a) + int(b)
print("the value of c is", c)

# know we learn about input and output
# input() is a built-in function that allows the user to input data from the keyboard.

name= input("enter your name: ")
age= input("enter your age: ")
print("your name is", name)
print("your age is", age)

# Some points for remamber is python the in put statements are always str and so for tha we are using some techniques to convert the str to int or float for example we can use int() or float() to convert the str to int or float.
Name = input("enter your name: ")
Age = int(input("enter your age: "))

print("your name is", Name)
print("your age is", Age)

#Task: Write a program that takes two numbers as input from the user and prints their sum, difference, product.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
print("sum:", sum)
print("difference:", difference)
print("product:", product)


#Task: Write a program that takes the radius of a circle as input from the user and prints the area of the circle.

radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area = pi * radius ** 2
print("The area of the circle is:", area)   

  

#task: Write a program that takes a number as input from the user and checks if it is even or odd.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


#task: Write a program that takes a string as input from the user and prints the number of characters in the string.

string = input("Enter a string: ")
length = len(string)
print("The number of characters in the string is:", length)
