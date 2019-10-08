def task_86_a():
    """Task 86_a: Have a natural number n how many digits in this number n"""

    n = input("Some natural number n, how many digits in this number n\n\n"
              "Enter n: ")
    answer = len(list(n))
    return answer


def task_86_b():
    """Task 86_b: Have a natural number n count the sum of all digits in number n"""

    n = input("Some natural number n, calculate the sum of all digits in this number n\n\n"
              "Enter n: ")
    list_of_digits = [int(digit) for digit in n]
    return sum(list_of_digits)
