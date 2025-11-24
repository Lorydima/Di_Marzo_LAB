# Lezione 24/11/2025 Calculator V2

# Library for calculator Dev
from colorama import Fore
import math

def calculator_introduction():
         print(Fore.YELLOW + "Python Calculator" + Fore.RESET)
         print(Fore.YELLOW + "Developed by Lorenzo Di Marzo 3E A.S 2025/26\n" + Fore.RESET)
         calculator_main_function_ask()

def calculator_main_function_ask():
     print("You want to use the simple calculator (+,/,*,/) or the advanced operations (sqrt,sin,cos)?")
     user_input = input("Insert command simple or advanced:")
     if user_input == "simple":
          calculator_main_function()
     if user_input == "advanced":
          calculator_advanced_function()

def calculator_advanced_function():
     while True:
          operations = input("Select operations (sqrt,sin,cos):")
          if operations == "sqrt":
               number = float(input("Insert number:"))
               sqrt = math.sqrt(float(number))
               print(str(sqrt))
          
          if operations == "sin":
               number = float(input("Insert number:"))
               sin = math.sin(float(number))
               print(str(sin))
          
          if operations == "cos":
               number = float(input("Insert number:"))
               cos = math.cos(float(number))
               print(str(cos))

def calculator_main_function():
    while True:
        number1 = float(input(Fore.BLUE + "\ninsert first number:" + Fore.RESET))
        operation = str(input (Fore.RED + "insert the operations (+,-,*,/):" + Fore.RESET))
        number2 = float(input(Fore.BLUE + "insert second number:" + Fore.RESET))
    
        if operation == "+":
            result = number1 + number2
            print(Fore.GREEN + str(result) + Fore.RESET)

        if operation == "-":
            result = number1 - number2
            print(Fore.GREEN + str(result) + Fore.RESET)

        if operation == "*":
            result = number1 * number2
            print(Fore.GREEN + str(result) + Fore.RESET)

        if operation == "/":
            result = number1 / number2
            print(Fore.GREEN + str(result) + Fore.RESET)

calculator_introduction()
