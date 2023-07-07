#Create a program that squares a number. Must be a function
def square(number):
    return number ** 2
number = int(input("INPUT: "))
squared = square(number)
print("OUTPUT: " + str(squared))