"""
Today we learn about file heandling in python 

when we need over python code not dlt in any system crash or any other issue  or save it for future then we use the file heandling



Today we learn
how we can open to a file
how we can read to a file
how we can write to a file
how we can close to a file
how we can dlt to a file

what is the file handing in python 

python can be used to perfom opertions on a file like (read and write data )



"""



#types of all files 
#1 text files : .txt ,.doc ,.log etc
#2 Binary files : .mp4,.mov, .png,.jpeg et



#open,read and close file for that we are doing that

#we have to open a file before reading or writing


#for open any file we  use a method
"""
f=open("file-IO.txt","r")# yaa paramter ma aya ga aik path of file or 2nd mod aya jo file ka upear kam krna han woh yani ki is ma kya kam krna pen krna read krna ya any thing else
# this way we can open any file 
data =f.read() #here if we pass 5 or 10 we get just what namber caharater we need to read showing 
print(data)
print(type(data))# this is optnal
f.close()

    
 #if i want to read one line at the type we need to write like that
f=open("file-IO.txt","r")
data=f.readline(2)

print(data)
f.close()

"""
#know we learn about how write something in the file 
#if we to want write anything in file 1st we need to open file then we can write any thing

#we can write any thing in file by using we waysf we pass "w" this is write mod and 2nd way is "a"
#"a" means we append at the end of file

"""


f=open("new_file.txt","w")

f.write("My name is faiza em a software enginer")

f.close()

#if we add some thing in any exeting file we can do that is this way

f=open("new_file.text","a")

f.write("em adding new line in file \n i'm currently learing python file heandling topice to day")

f.close()
"""

#if we want to werite in file at the start we can use R+ mood 

f=open("file-IO.txt","r+")
f.write( "I am faizan")
f.close()


"""
some importain points 

r+ we use for read + write and pointer will be in start and not existing data dlt or rewirte
 
w+ we use for read write the file data wil be dlt anf again need to write

a+ we can use for read append and the pointer will be the end and no data rew rite



"""

# know we will lean about how dlt the file in python 

# In python we can not dlt a file just using function or command  for that we useing modula for that 

#so for fata we mostly useing the module name =>os in python 
#using the os module 
"""

sytex=>

import os 

os.remove(filename)





f=open("new_file.txt","w")

f.write("My name is faiza em a software enginer")

f.close()

#if we add some thing in any exeting file we can do that is this way

f=open("new_file.text","a")

f.write("em adding new line in file \n i'm currently learing python file heandling topice to day")

f.close()

import os

os.remove("new_file.txt")#path or name file 






All the perfoming work ding at previsouly

we can also doing that some fuction name is 

is with

syntax

with open("demo.txt,"a") as f:

data=f.read()


"""


#some practice question 

"""
creat a new file"parctuce.txt" using python
,Add the following data in it:
Hi ali 
we are learing python today
using file heandiling 
today topice is that we have 
i like programing in java 
"""

with open("practice.txt", "w") as f:
    f.write("Hi ali\n")
    f.write("we are learning python today\n")
    f.write("using file handling\n")
    f.write("today topic is that we have\n")
    f.write("i like programming in java\n")
  


    # know WAP that replace occurrence of python with java in above file

with open("practice.txt", "r") as f:
        data = f.read()

new_data = data.replace("python", "java")

with open("practice.txt", "w") as fw:
        fw.write(new_data)

print(new_data)


#seacrch if the word "learing" exists in the file or not

with open("practice.txt","r") as f:
    data = f.read()
    word = "learing"
    if data.find(word) != -1:
        print("found")
    else:
        print("not found")


