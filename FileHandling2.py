# This is to demonstrate how to push changes in a file
# Lower Case Function
def process_lower(text):
    print("I'm in process of lower block.")
    lowerCase = text.lower()
    return lowerCase

file_name = input("Enter the file name that you want to process: ")

with open(file_name, "r") as file:
    print(f"I'm reading, {file_name}.")
    content = file.read()

result = process_lower(content)
print("Result: ", result)