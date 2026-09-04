def get_number(message):

    while True:

        number = input(message).strip()

        if not number:
            print("Number cannot be empty. Please enter a number.")
            continue

        try:
            number_float = float(number)

        except ValueError:
            print("Wrong input format. Try again.")
            continue

        if not -100 <= number_float <= 100:
            print("Chosen number not in range <-100, 100>.")
            continue

        return number_float


def get_operation(message):

    allowed_operations = {"+", "-", "*", "/"}

    while True:

        operation = input(message).strip()

        if not operation:
            print("Operation cannot be empty.")
            continue

        if operation not in allowed_operations:
            print(f'Operation not in allowed operations.\n{allowed_operations}.')
            continue

        return operation

if __name__ == "__main__":

    first_number = get_number("First number: ")
    second_number = get_number("Second number: ")
    operation = get_operation("Operation: ")