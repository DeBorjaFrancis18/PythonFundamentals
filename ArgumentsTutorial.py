#Function that sums infinite numbers
def summationOf(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
print(summationOf(1,2,3,4,5,6,7,8,9,10))