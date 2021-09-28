#user input
print("Enter Your Number: ")
userinput = input()
print("You Entered : ",userinput)

#print("Your number: ",userinput + 10)#its an error becouse your entered number is not a integer its a string
print("Your number : ",int(userinput) + 10) #This will not give any error, it will calculate it

#Quiz :- Write a program which can take 2 input and add them
print("Enter 1st number: ")
firstinput = input()
print("Enter 2nd number: ")
secondinput = input()
print("Sum of these two numbers is :",int(firstinput)+int(secondinput))

