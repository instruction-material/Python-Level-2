def add(left, right):
    return left + right


def subtract(left, right):
    return left - right


def multiply(left, right):
    return left * right


def divide(left, right):
    return left / right


def remainder(left, right):
    return left % right


def factorial(number):
    if not 0 <= number <= 100:
        raise ValueError("Use a factorial input from 0 through 100.")
    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result


def power(base, exponent):
    if not 0 <= exponent <= 100:
        raise ValueError("Use an exponent from 0 through 100.")
    return base**exponent


def read_number(prompt):
    try:
        number = int(input(prompt))
    except ValueError:
        raise ValueError("Enter a whole number.") from None
    if not -1000 <= number <= 1000:
        raise ValueError("Use whole numbers from -1000 through 1000.")
    return number


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": remainder,
    "^": power,
}

while True:
    operator = input("Operation (+, -, *, /, %, ^, !, or q): ").strip().lower()
    if operator == "q":
        break
    if operator != "!" and operator not in operations:
        print("Choose a listed operation.")
        continue
    try:
        left = read_number("First whole number: ")
        if operator == "!":
            print(f"{left}! = {factorial(left)}")
        else:
            right = read_number("Second whole number: ")
            print(f"{left} {operator} {right} = {operations[operator](left, right)}")
    except ZeroDivisionError:
        print("Division and remainder require a nonzero second number.")
    except ValueError as error:
        print(error)
