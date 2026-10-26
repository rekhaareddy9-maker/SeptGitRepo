# Lower Case Function
def process_lower(text):
    print("I'm in process of lower block")
    lowerCase = text.lower()
    return lowerCase

# Open the File
# C:\Users\HP PC\AppData\Local\Programs\RRSeptDemo\input.txt (Path)

# input.txt
file = open("input.txt", "r")

# Read the File
content = file.read()

# Print the Content
print("Content: ", content)

# Print the result
result = process_lower(content)
print("Result: ", result)