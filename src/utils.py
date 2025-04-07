def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división por cero"


def remove_duplicates(numbers):
    return list(set(numbers))