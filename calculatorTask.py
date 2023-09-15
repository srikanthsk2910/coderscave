# Python program for simple calculator
 
# Function for addition of 2 numbers
def add(number1, number2):
    return number1 + number2
 
# Function for substraction of 2 numbers
def subtract(number1, number2):
    return number1 - number2
 
# Function for multiplication of 2 numbers
def multiply(number1, number2):
    return number1 * number2
 
# Function for division of 2 numbers
def divide(number1, number2):
    return number1 / number2
 
print("Do select the operation to be performed :\n" \
        "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n")
 
 
#taking the input
choice = int(input("Select the operations from 1, 2, 3, 4 :"))
 
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
 
if choice == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
 
elif choice == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
 
elif choice == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
 
elif choice == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input = error")

