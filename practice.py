# Kentavious Mack, Use this as a file to practice code you cannot understand

values = []
NUM_INTEGERS = 10

while len(values) < NUM_INTEGERS:
    userInput = int(input("Enter a number: "))
    if userInput not in values :
        values.append(userInput)
print("The numbers are", values)