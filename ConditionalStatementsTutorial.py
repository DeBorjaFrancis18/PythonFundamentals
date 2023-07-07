print("Enter grades per subject")
math = int(input("Math: "))
science = int(input("Science: "))
english = int(input("English: "))
average = (math + science + english)/3
print("average: " + str(average))

if average > 100 or average < 50:
    print("Invalid Grade")
elif average >= 98:
    print("With Highest Honor")
elif average >= 95:
    print("With High Honor")
elif average >= 90:
    print("With Honor")
elif average >= 75:
    print("Passed")
else:
    print("Failed")