# Lezione 27/10/2025 Calculator

def calculator_main_function():
    print("Python Calculator\n")
    number1 = float(input("insert first number:"))
    operation = str(input ("insert the operations (+,-,*,/):"))
    number2 = float(input("insert second number:"))
   
    if operation == "+":
        result = number1 + number2
        print(result)

    if operation == "-":
        result = number1 - number2
        print(result)

    if operation == "*":
        result = number1 * number2
        print(result)

    if operation == "/":
        result = number1 / number2
        print(result)    

calculator_main_function()