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


def task330():
    """Task 330 Have a number n. find all ideal number lower then n"""

    n = input("Enter n: ")
    n = int(n)
    list_of_numbers = []
    for i in range(0, n):
        number = 0
        for j in range(1, i):
            if i % j == 0:
                number += j
        if number == i:
            list_of_numbers.append(i)
    return list_of_numbers