courseStudents = [
    ["BSECE", ["Francis","Noaim"]],
    ["COED", ["Andrea","Carl","Lem"]],
    ["BSVALO", ["Baniqued","Mel","Carl"]]
    ]
for listCourse in courseStudents:
    print(listCourse[0])
    for listStudent in listCourse[1]:
        print("  -", end="")
        print(listStudent)
    print()