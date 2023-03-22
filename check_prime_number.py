def check_prime_number(num):
    if num < 1:
        return False

    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False

    return True


if __name__ == '__main__':
    number = 12
    print(check_prime_number(number))
