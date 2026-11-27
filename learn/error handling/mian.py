print("init............")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
try:
    print("the val of a/b is:", a/b)
except ZeroDivisionError:
    
    print("division by zero is not possible")
finally:
print("end.............")