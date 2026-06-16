#Today we will learn about the strind data type in python ans conditional statements

#String data type
#A string is a sequence of characters enclosed in single quotes, double quotes, or triple quotes E.G IT CAN BE CHARACTER, WORD, OR SENTENCE

str1 = "faizan"
str2 = 'faizan'
str3 = """faizan"""
str4 = "generally we use double quotes for string data type but we can also use single and triple quotes"

#we can use /n for new line in string data type
str5 = "hello\nworld"
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
  
#we can also use + operator to concatenate two strings
str6 = str1 + " " + str4    
print(str6)

#also we use len() function to find the length of a string
length = len(str4)  
print(length)


#know we will learn about indexing in string data type
#Indexing starts from 0 in python
print(str1[0])  #it will print the first character of the string
print(str1[1])  #it will print the second character of the string
print(str1[-1]) #it will print the last character of the string


#we can also use slicing to get a substring from a string
print(str1[0:3])  #it will print the first three characters of the string
print(str1[3:6])   #it will print the characters from index 3 to 5
#we can also use step in slicing to get every nth character from a string
print(str1[0:6:2])  #it will print every second character from index 0 to 5

#using the indexing in string we can not change the value of a string because strings are immutable in python
#str1[0] = "F"  #it will give an error because we cannot change the value of a string using indexing
 
# but we can change the value of a string by concatenating it with another string
str1 = "F" + str1[1:]  #it will change the first character of the string to "F"
print(str1)



#know we will learn about the string function in python
#we can use the upper() function to convert a string to uppercase
str7 = str1.upper() 

print(str7)

#we can use the lower() function to convert a string to lowercase
str8 = str7.lower() 
print(str8)

#we can use the strip() function to remove the leading and trailing whitespace from a string
str9 = "   hello world   "
str10 = str9.strip()
print(str10)

#we can use the replace() function to replace a substring with another substring in a string
str11 = str10.replace("hello", "hi")
print(str11)

#we can use the endwith() function to check if a string ends with a specific substring
str12 = "hello world"
print(str12.endswith("world"))  #it will return True because the string ends with "world"
print(str12.endswith("hello"))  #it will return False because the string does not end with "hello"

#means that if the string ends with the specified substring it will return True otherwise it will return False

# we can also use the capitalize() function to capitalize the first character of a string
str13 = "hello world"
str14 = str13.capitalize()
print(str14)  #it will print "Hello world" because the first character of the string is capitalized


# we can also use thr replace() function to replace a substring with another substring in a string
str15 = "hello world"
str16 = str15.replace("world", "python")
print(str16)  #it will print "hello python" because the substring "world" is replaced with "python"

# we can also use the find() function to find the index of the first occurrence of a substring in a string
str17 = "hello world"
index = str17.find("world")
print(index)  #it will print 6 because the substring "world" starts at index 6

# we can also use the count() function to count the number of occurrences of a substring in a string
str18 = "hello world"   
count = str18.count("o")
print(count)  #it will print 2 because the substring "o" occurs twice in the string



# lets do some practice problems on string data type

#WAP to input user's name and print it length
name = input("Enter your name: ")
name_length = len(name)
print("The length of your name is:", name_length)

#WAP to input a string and check if it starts with "hello"
string = input("Enter a string: ")
if string.startswith("hello"):
    print("The string starts with 'hello'")
else:
    print("The string does not start with 'hello'")

    #WAP to find the occurence of '$' in the sting
 
string = input("Enter a string:")
count = string.count("$")
print("The number of occurrences of '$' in the string is:", count)  


#know we will learn about the conditional statements in python

#syntex of if statement
#if condition:
    #code to be executed if the condition is true
#syntex of if-else statement
#if condition:

    #code to be executed if the condition is true
#else:
    #code to be executed if the condition is false
#syntex of if-elif-else statement
#if condition1:
    #code to be executed if condition1 is true
#elif condition2:

    #code to be executed if condition2 is true

#else:


    #code to be executed if both condition1 and condition2 are false

#WAP to input a number and check if it is positive, negative or zero
number = float(input("Enter a number: "))       
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")



#lets do some practice problems on conditional statements

#WAP to input a number and check if it is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


    #WAP to input a year and check if it is a leap year or not
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")



#WAP to find greatest of 3 number entered by user

    num1 =float(input("Enter first number: "))
    num2 =float(input("Enter second number: "))
    num3 =float(input("Enter third number: "))
    if num1 >= num2 and num1 >= num3:
        print("The greatest number is:", num1)
    elif num2 >= num1 and num2 >= num3:
        print("The greatest number is:", num2)
    else:
        print("The greatest number is:", num3)

    """
The : (Colon): This is mandatory in Python. It signals the end of the if condition and the start of the indented code block that follows.

The () (Parentheses): These are optional. In Python, you only really use them when you need to override or clarify the order of operations in complex, multi-part conditions (like in your leap year example)."""