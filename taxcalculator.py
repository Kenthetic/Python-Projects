# Author: Kentavious Mack, Date: September 14th 2026, Tax Calculator

status = input("Enter your filing status (single or married): ")
income = int(input("Enter your income in integer form: "))

if income < 0 :
    print("Invalid income amount.")
elif status == "single" and income <= 32000 :
    tax = income * 0.10
    print("Your tax is 10% of your income, which is: ", tax)
elif status == "single" and income > 32000 :
    tax = income * 0.25
    print("Your tax is 25% of your income, which is: ", tax)
elif status == "married" and income <= 64000 :
    tax = income * 0.10
    print("Your tax is 10% of your income, which is: ", tax)
elif status == "married" and income > 64000 :
    tax = income * 0.25
    print("Your tax is 25% of your income, which is: ", tax)
else :
    print("Invalid input. Please enter single or married for filing status ans a valid income amount.")
