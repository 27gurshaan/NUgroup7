# This function adds two numbers
import Addition
import Subtraction
import Multiplication
import Division

# This is to present a menu to the user
print("Select operation.")
print("1.Addition")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", Addition.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Subtraction.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", Multiplication.multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", Division.divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
