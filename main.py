import inputs, calculations

def main():

    print("=== Welcome to the CLI calculator ===")
    print("This calculator lets you add(+), subtract(-), multiply(*) and divide(/) your numbers.")
    print("Numbers that you can operate on are in (-100) to (100) range.")
    print("")

def main():

    operation = inputs.get_operation("Enter operation: ")
    first_number = inputs.get_number("Enter first number: ")

    while True:
        second_number = inputs.get_number("Enter second number: ")

        if operation == "/" and second_number == 0:
            print("You can't divide by zero")
            continue

        break

    result = calculations.calculator_operation(first_number, second_number, operation)

    print("")
    print(f'Result of "{operation}" operation on {first_number} and {second_number} is {result:.3f}')

    print("")
    print("=== Thanks for using our calculator ===")

if __name__ == "__main__":
    main()