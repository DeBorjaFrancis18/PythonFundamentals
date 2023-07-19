evenNumbers = {2, 4, 6, 8, 10}
oddNumbers = {1, 3, 5, 7, 9}
copySet = evenNumbers.copy() #copy of set 1
countingNumbers = oddNumbers.union(evenNumbers) #union of 2 sets
evenNumbers.add(12)

even = list(evenNumbers)
even[0] = "hotdog"
print(f"list copy: {even}") #di kasama yung latest update ng set
evenSet = set(even) #convert list to set
print(evenSet)

evenNumbers.update([14,16,18,20])
evenNumbers.remove(6) #delete specific item
evenNumbers.add("six") #add string into set of integers
evenNumbers.pop() #delete the first item in set
for number in evenNumbers:
    print(f"indiv: {number}") #prints individual number in set

newSet = evenNumbers.difference(copySet)
print(f"diff1: {newSet}") #prints difference between 2 sets

anotherSet = copySet.difference(evenNumbers)
print(f"diff2: {anotherSet}") #prints difference between 2 sets

commonInSet = evenNumbers.intersection(copySet)
print(f"common: {commonInSet}") #prints intersection between 2 sets

Symmetric = copySet.symmetric_difference(commonInSet)
print(f"Symmetric: {Symmetric}")

print(f"disjoint: {evenNumbers.isdisjoint(oddNumbers)}") #has no same element

print(f"Subset: {oddNumbers.issubset(countingNumbers)}")

print(f"Superset: {countingNumbers.issuperset(oddNumbers)}")

evenNumbers.clear() #removes all value in a set
print(evenNumbers) #prints null set
print(countingNumbers)