# Kentavious Mack, September 9th 2026, Decision Making in Python

#Checking the dates temperature and printing output based on the input
temp = int(input("Enter todays Temperature: "))

if temp >= 80:
    print("Today is hot, drink water")
else: 
    print("Today is not that hot, you do not need water")

#Checking if a number is odd or even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Checking if a number is odd or even but reverse of above
num = int(input("Enter a number: "))
if num % 2 != 0:
    print("The number is odd")
else:
    print("The number is even")

#Customer orders a drink, lets check what they want and if they are old enough to get alcohol

drink = input("What would you like to drink: Coke or Wine? ")
age = int(input("What is your age?"))

if drink == "Coke":
    print("Here is your Coke, Thanks for shopping.")
if drink == "Wine" and age >= 21:
    print("Here is your Wine, Thanks for shopping.")
else:
    print("You are not old enough to purchase Wine.")

#Lets see if number 1 is greater than number 2 
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 > num2:
    print("Number 1 is greater than Number 2")

elif num2 > num1:
    print("Number 2 is greater than Number 1")
else:
    print("Both are equal")

#Check the students grade
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("You recieved an A")
elif grade >= 80:
    print("You recieved a B")
elif grade >= 70:
    print("You recieved a C")
elif grade >= 60:
    print("You recieved a D")
else:
    print("You recieved an F")

