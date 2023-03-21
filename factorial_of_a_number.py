def factorial_of_number(num):
    factorial = 1
    if num < 0:
        return "Factorial for number 0 does not exist"
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
    return factorial


if __name__ == '__main__':
    number = 7
    print(factorial_of_number(number))
