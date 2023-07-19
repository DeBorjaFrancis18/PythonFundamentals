studentOneTraits = {
    "Height" : 163,
    "Weight" : 64.5,
    "Skin" : "Brown"
}

studentTwoTraits = {
    "Height" : 145,
    "Weight" : 50.5,
    "Skin" : "Brown"
}

studentOne = {
    "Name" : "Francis",
    "Course" : "BSECE",
    "Age" : 23,
    "Game" : "Valorant",
    "Physical" : studentOneTraits
}

studentTwo = {
    "Name" : "Andrea",
    "Course" : "COED",
    "Age" : 23,
    "Game" : "Mobile Legends",
    "Physical" : studentTwoTraits
}

students = [studentOne, studentTwo]

print(f"key: {studentOne['Name']}") #prints key
print(f"get: {studentOne.get('Name')}")

studentOne["Name"] = "Johnny" #changes item in a dictionary
print(f"New Name: {studentOne['Name']}")
print(f"size: {len(studentOne)}") #print dictionary size

studentOne["Gender"] = "Male" #add non-existing key-value
print(f"Student 1: {studentOne}")

studentOne.pop("Age") #deletes key
print(f"no age: {studentOne}")

print(students[0].get("Physical"))

studentOne.popitem()
print(f"pop-item no gender: {studentOne}")