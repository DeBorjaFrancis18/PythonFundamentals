studentOneTraits = {
    "Height" : 163,
    "Weight" : 64.5,
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
    "Game" : "Mobile Legends"
}

students = [studentOne, studentTwo]

print(students[0].get("Physical"))