num1 = float(input("enter the first number :"))
num2 = float(input("enter the second number :"))
Addition = num1 + num2
Substraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else :
     division = "Undefined (cannot divide by zero)"
print("results :")
print(f"Addition : {num1} + {num2} = {Addition}")
print(f"Substraction : {num1} - {num2} = {Substraction}")
print(f"Multiplication : {num1} * {num2} = {multiplication}")
print(f"Division : {num1} / {num2} = {division}")