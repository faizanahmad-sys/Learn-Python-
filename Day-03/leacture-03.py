#Today in chapter 3 we will learn about list and Tuples
# the list in python is that A build type stores set of value
#it can store element different type of  (integer,float,string,etc)

#eg

marks = [10,20,30,59]
student = ["ali",45.5,100]
print(type(marks))
print (marks)
print(marks[0])
print(student[0])
print(len(student))

#we can not print like marks([0],[3]) in pyton 
#In python string are immutable and list are mutable this the important point ie

student[0] ="faizan"
print(student)


#know how we do sclicig in list ie

let_marks = [1,2,3,4,5]
print(let_marks[1:3])
#also we can do that 
print(let_marks[-3: -4])

# know we learn about some funtions in list
#ie
list =[1,2,3,4]
list.append(4)# add one element at the end[2,1,3,4]
list.sort() #sort in ascending order [3,2,1]
list.sort(reverse=True)# sort in descending order [3,2,1]
list.reverse()#reverses list [3,1,2]
#list.insert(idx,el) #insert element at index means that index one pa koi value add krna or jo elemnat add krna han woj bd ma aya ga like
list.insert(2, 5)



#know we will learn about the tuple
#tuple are just like list but tuple are immutable like sting in python
 #ie
tup=(1,2,3)
print(tup)
print(tup[0])
print([2])
tup1=()
print(tup1)
print(type(tup1))



#let do some pratis question   relate to the topice
#some we some understing the concepts

#WAP to ask user to enter name of their favorit movies and store them in a list

user = input("enter your favorit movies name ")
list.append(user)
print(list) 
