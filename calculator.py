



num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

Additional = num1 + num2
difference = num1 - num2
product = num1 * num2

print("the sum of", num1, "and", num2, "is:", Additional)
print("the difference of", num1, "and", num2, "is:", difference)
print("the product of", num1, "and", num2, "is:", product)

if num2 == 0:
    print("division by zero is not possible")
else:
    division = num1 / num2
    print("the division of", num1, "and", num2, "is:", division)
