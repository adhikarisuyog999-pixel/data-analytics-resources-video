# store unique value in a group
# doesnt allow duplicate values


set1 ={2,4,6,8,2,4}
print(set1)

set2=(1,3,5,7,9)
set1.update([100,123])# random placement

print(set1)

# set2.remove(3)
# set2.discard(3)
print(set2)

# set2.clear()
print(set2)

#set operations

result = set1.union(set2)
print(result)
result2= set1.intersection(set2)
print(result2)