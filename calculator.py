print(input("Press 'ENTER' to get into the calculator"))

num1 = float(input("Enter a number:"))
operator = input("Enter a operator:'+','-','*','%':")
num2 = float(input("Enter a second number: "))


if operator == '+':
    print("The total is", num1 + num2)
elif operator == '-':
    print("The total is", num1 - num2)
elif operator == '*':
    print("The total is", num1 * num2)
elif operator == '%':
    print("The total is", num1 % num2 )
else:
    print("This operator cannot be involved")
