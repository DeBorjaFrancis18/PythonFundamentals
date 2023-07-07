lives = 3
print("What is a number when multiplied by itself becomes twice itself?")
print("(answer must be in words)")
while lives > 0:
    answer = (input("Answer: "))
    if answer == "two" or answer == "Two" or answer == "TWO":
        print("You are correct!")
        break
    else:
        print("Wrong Answer!")
        lives = lives - 1
        print(str(lives) + " live/s remaining")
if lives == 0:
    print("Game over, you dumb!")