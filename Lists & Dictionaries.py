# Lists
Persons = ["Ganesh", "Srini", "Mani", 15, 32.6, True]
print("Part 1: ", Persons)
print("Part 2: ", Persons[0])

# Dictionaries
users = [{"Name" : "Ganesh", "Course" : "Gen AI", "Exp" : 15},
{"Name" : "Srini", "Course" : "Gen AI", "Exp" : 18 },
{"Name" : "Sarath", "Course" : "Gen AI", "Exp" : 14 },
{"Name" : "Rekha", "Course" : "Gen AI", "Exp" : 19 }]

print("Part 3: ", users)
print("Part 4: ", users[1]["Name"])
print("Part 5: ", users[5]["Name"]) # Error because index 5 is out of range, as there are only 4 users in the list (indices 0 to 3)..
print("Part 6: ", users[2]["Exp"])

# Conditions & Loops
if users[2]["Exp"] >= 15:
    print("Part 7: ", users[2]["Name"])
    print("Part 8: ", users[2]["Course"])
else:
     print("No users above 15 years of experience.")

for user in users:
    if user["Exp"] >= 15:
        print(f"Part 9: {user["Name"]}, {user["Course"]} that users above 15 years of experience.")
    else:
        print(f"Part 10: {user["Name"]}, {user["Course"]} that no users above 15 years of experience.")