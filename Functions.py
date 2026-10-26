# Functions Demo
 
# Define Variable
Person = "Rekha"
FirstName = "Rekha"
LastName = "Reddy"
sessionNumber = 9
sessionNumber2 = "9"

# Define Function
def calculateCost(sessionNumber):
    sessionCost = 10
    TrainingCost = sessionNumber * sessionCost
    return TrainingCost

def fullName(fName, lName):
    output = fName + " " + lName
    ##output = f"{fName} {lName}"
    return output

def gName(fName, sessionNumber2):
    output = fName + sessionNumber2
    return output

# Execute the function
Result = calculateCost(sessionNumber)
Result2 = fullName(FirstName, LastName)
Result3 = gName(FirstName, sessionNumber2)

# Print the result
print("Result: ", Result)
print("Result 2: ", Result2)
print("Result 3: ", Result3)