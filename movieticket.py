# Kentavious Mack, September 14th 2026, Movie Ticket Price Calculator

age = int(input("Enter your age: "))
ticket_price = 12.00
discount_senior = 0.30
discount_child = 0.50
is_student = input("Are you a student?: ").lower()

if is_student == "yes":
    ticket_price = ticket_price - 2

if age <= 12:
    ticket_price = ticket_price * (1 - discount_child)
elif age >= 65:
    ticket_price = ticket_price * (1 - discount_senior)

print("Your ticket price is: ", ticket_price)
