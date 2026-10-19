#Kentavious Mack, September 28th, 2026
#Finding the average of userInput


#Purpose: 
# @param numbers
# @ return average
def averageOfFive(num1, num2, num3, num4, num5) :
    average = num1 + num2 + num3 + num4 + num5 // 5
    return average


#Purpose: control the averageOfFive function
#@param none
#@return none
def main() :
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    num3 = int(input("Enter a number: "))
    num4 = int(input("Enter a number: "))
    num5 = int(input("Enter a number: "))
    result = averageOfFive(num1, num2, num3, num4, num5)
    print(result)

main()