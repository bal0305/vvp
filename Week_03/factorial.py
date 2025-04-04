def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
factorial_loop(20)  # test with a number
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
factorial_recursive(20)  # test with a number
