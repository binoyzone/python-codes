def sort_list(num_list):
    n = len(num_list)
    for i in range(n-1):
        for j in range(0, n-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list


if __name__ == '__main__':
    number_list = [64, 34, 25, 12, 22, 11, 90]
    print(sort_list(number_list))
