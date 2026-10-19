# Kentavious Mack, September 16th 2026, Password Attempts

#Give user incorrect until password is correct after 3 lock them out

password = "python123"
attempts = 0
successAttempt = False

while attempts < 3 :
    user_input = input("Enter your password: ")
    attempts = attempts + 1
    if user_input == password :
        print("Logging in...")
        successAttempt = True
        break
    else :
        print("Incorrect try again.")
if not successAttempt : 
    print("You have been locked out.")