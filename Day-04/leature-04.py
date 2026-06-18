#Today we will learn about the dictionary and set
#dictionary in p are used to store data value in key:value pairs
# they are unorder,mutable and changeable and don't allow duplicate keys
#ie
info ={
    "key":"value",
    "learing" :"coding python",
    "name" : "ali",
    "marks":100,
    "subject": ["alii","c","python"],
    
}
print(info)#also we can do that
print(info["subject"])
print(info["name"])


""" so the final just remamber the the sytex of dictnaray how we will creating that 

 #name{
 # key" :" value" ,
 "num": 24,
 }
"""
#we can do nesting in dictinoary like

dict= {
 "subject" : "python",
 "student" :{
     "name" : "faizan",
     
     "from" : "gilgit",
     
 }

}

print(dict["student"]["name"])

#some funtion in dictnary we are using 

print(dict.keys()) # returns all keys

print(list(dict.values()))# retuns all values

print(dict.items())# returns all (key,val) pairs as tuples

print(dict.get("name"))  #not through ana error just show none

#how update any dictionary
new_dictionary ={"name" : "shah"}
dict.update(new_dictionary)

print(dict)


# know we learn about the set in python 


#ser is the collection of the unordered items

# Each element in the set must be unique and immutable

#set1 ={1,2,3,4,}
#set2 = {1,2,2} # THIS THROUGH THE ERROR BC OF REPEATED VALUE sho just doing {1,2}

#null_set = sett{}# this also wrong
# so we can store any value in set but not store list and dictionary in set bc that are immutaable

set ={1,2,"ali", "shah",}
print(set)

#what id the value are repeate then what will be happens

set2 = {1,2,3,3,"ali","ali",}# set just ignore the repeating value
print(set2)

#set is not flw any oder they just print the value remdom output order

# know how we make empty set 

set3 = set()
print(type(set3))


#some methord in set are 
# set. add (el) that add in the element 
# set,remove(el) that just remove elemnt form set
# set.clear() that empties the set
# set.pop() removes a remdom value

# how to use the set methord 


let_set.add(1)
let_set.add (2)
let_set.remove(1)
let_set.clear()
let_set.add(1,2,4,5)
#let_set.pop() we can not use pop funtion like this so
print(let_set.pop())

#here some imp methord in set that are the union and intersection
# how use that 
set0 ={1,2,4,"ali"}
seT1 = {2,3,4,"shah"}

print (set0.intersection(seT1))
print(set1.union(seT1))



# let do some practice question

#store following word meaning in python dictionary

dict ={

"name" :"ali",
"shah" : "acha banda ",
"car ": "cat is small",

}

print(dict)


# you are given a list of subject for student . Assume one classroom is required for 1 subject
#how many clssrooms are needed by all student


set= {
"html", "c++", "python", "html" ,"C#","css"
}
print(len(set))