def get_sum_of_pair(arr_list):
    n = len(arr_list)
    sum_arr = []
    for i in range(0, n, 2):
        if i + 1 < n:
            curr_item = arr_list[i]
            next_item = arr_list[i + 1]
            sum_arr.append(curr_item + next_item)
        else:
            sum_arr.append(arr_list[i])
    return sum_arr


if __name__ == '__main__':
    print("From given list create a new list with sum of pair and if no pair exist return the single integer")
    number_list = [1, 2, 3, 4, 5, 6, 7]
    print(get_sum_of_pair(number_list))
