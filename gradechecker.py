#Kentavious Mack, September 30th, 2026

#Create a function that finds if the user got A B C D or F

def gradeChecker(score) :
    if userInput >= 90 and userInput <= 100 :
        print("A")
    elif userInput >= 80 and userInput <= 89 :
        print("B")
    elif userInput >= 70 and userInput <= 79 :
        print("C")
    elif userInput >= 60 and userInput <= 69 :
        print("D")
    else :
        print("F")

gradeChecker()
