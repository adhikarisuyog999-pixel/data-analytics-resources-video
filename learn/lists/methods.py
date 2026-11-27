items =['a','b','c','d']
items.append("e")# adds e at next index
print(items)
items.insert(0,"z")
print(items)

items.pop(0)
print(items)
print(items.index("a"))

numbers=[1,3,5,2,77,44,22]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)#decreasing order
print(numbers)


print(15 in numbers)# check if 15 is in numbers or not