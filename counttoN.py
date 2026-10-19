#Kentavious Mack, September 30th, 2026

#This code counts from 1 to N

def nCounter() :
    userInput = int(input("Enter a number 1-5: "))
    for count in range(1, userInput + 1) :
        print(count)

nCounter()