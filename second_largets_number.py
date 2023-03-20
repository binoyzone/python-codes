def print_largest_number(nums):
    largest_num = 0
    second_largest_num = 0

    if nums[0] > nums[1]:
        largest_num = nums[0]
        second_largest_num = nums[1]
    else:
        largest_num = nums[1]
        second_largest_num = nums[0]
    for i in range(2, len(nums)):
        if nums[i] > largest_num:
            second_largest_num = largest_num
            largest_num = nums[i]
        elif nums[i] > second_largest_num:
            second_largest_num = nums[i]

    return second_largest_num


if __name__ == '__main__':
    number_list = [3, 4, 5, 2, 7, 1, 6]
    print(print_largest_number(number_list))
