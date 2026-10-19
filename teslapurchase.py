# Kentavious Mack, Date: September 14th 2026, Tesla Purchase Calculator

model = input("Enter the Tesla model you want to purchase (S, 3, X, Y): ")
purchaseType = input("How would you like to pay (Cash or Finance): ")
model3PerformanceCash = 54990
model3PerformanceFinance = 789
modelYPerformanceCash = 57990
modelYPerformanceFinance = 884

if model == "S" or model == "X" :
    print("The Tesla Model S and Model X are discontinued and are no longer available for purchase.")

elif model == "3" and purchaseType == "Cash" :
    print("The Tesla Model 3 Performance Cash price is: $", model3PerformanceCash)

elif model == "3" and purchaseType == "Finance" :
    print("The Tesla Model 3 Performance Monthly payment is: $", model3PerformanceFinance)

elif model == "Y" and purchaseType == "Cash" :
    print("The Tesla Model Y Performance Cash price is: $", modelYPerformanceCash)

elif model == "Y" and purchaseType == "Finance" :
    print("The Tesla Model Y Performance Monthly payment is: $", modelYPerformanceFinance)
else :
    print("Invalid input.")
