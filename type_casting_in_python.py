#type casting
#with type casting we can change the type of varible 
#we can change the type of an variable using type casting like this
print(int(var5)+int(var6))   #here we have changed the type of the variable var5 and var6 using type casting
#we have more function like this 
"""
str()    - it will change any variable to string
int()    - it will change any variable to integer
float()  - it will change any variable to floating number 

"""

#if we have to print any thing more than 1 time we can use like this
print(10* "Hello, World! ")    #it will print Hello, World! 10 times
#if we have to print in this in different line we can use'\n'
print(10* "Hello, World!\n")       #it will print Hello, World! 10 times in different line
#this is privious one
print(10* int(var5)+int(var6))   #but it will not print result 10 times #it will multiply the result with 10
#if we have to print result 10 times we have to chanhge result in string like this 
print(10* str(int(var5)+int(var6))) #this will print result ten times
