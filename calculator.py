operator = input("ENTER an operator (+ - * /) ")
num1= float(input("Enter 1st number:"))
num2= float(input("Enter 2nd number:"))
num3= float(input("Enter 3rd number:"))



if operator == "+":
   
    result = +num1 + num2 + num3
    print(round(result, 3))
if operator == "-":
    result = num1 - num2 - num3
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2 * num3
    print(round(result, 3))
elif operator =="/":
    result = num1 / num2 / num3
    print(round(result, 3))


else:
    [print(f"{operator} is not valid operator")]
