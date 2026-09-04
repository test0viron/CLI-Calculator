import inputs, calculations

def main():

    first_number = inputs.get_number("Enter first number: ")
    second_number = inputs.get_number("Enter second number: ")
    operation = inputs.get_operation("Enter operation: ")

    result = calculations.calculator_operation(first_number, second_number, operation)

    return first_number, second_number, operation, result

first_number, second_number, operation, result = main()

print(f'Result of "{operation}" operation on {first_number} and {second_number} is {result}')
