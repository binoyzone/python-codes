def print_largest_number(nums):
    largest_num = 0
    for num in nums:
        if num > largest_num:
            largest_num = num

    return largest_num


if __name__ == '__main__':
    number_list = [3, 4, 5, 2, 7, 1, 2]
    print(print_largest_number(number_list))
