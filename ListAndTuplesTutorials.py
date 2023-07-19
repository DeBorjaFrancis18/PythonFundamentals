courses = ["BSIT", "BSECE", "BLIS", "BSCpE"]
food = ["Burger", "Candy", "Pizza"]
alphabet = ['a', 'd', 's', 'w', 'b']
numbers = [2, 4, 6, 3, 7, 8, 1]
courses[0] = "Hatdog"
courses.append("BSValo") #add at the last element
courses.insert(5, "Hatdog") #add at specific index
print(courses[0])
print(f"size: {len(courses)}")
print(courses.count("Hatdog"))

alphabet.sort() #sorts list ascending order
print(f"sort: {alphabet}")

numbers.sort(reverse=True) #sorts list in descending order
print(f"rev-sort: {numbers}")

food.reverse() #reverses list
print(f"reverse: {food}")

combined = courses + food #combines 2 list
print(f"combined: {combined}")

courses.append(food)
print(f"append: {courses}")

print(f"Nested: {courses[6][1]}")

courses.remove("Hatdog") #deleting specific item from list
print(f"removed: {courses}")

courses.pop() #remove the last item from list
print(f"popped: {courses}")

del courses[3] #delete specific item from list
print(f"delete: {courses}")

courses.clear() #clear whole list
print(f"cleared: {courses}")