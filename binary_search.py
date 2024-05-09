def binary_search(target, list_of_data):
    list_len = len(list_of_data)
    lower_bound = 0
    upper_bound = list_len - 1
    while lower_bound <= upper_bound:
        middle_val = (lower_bound + upper_bound) // 2
        if list_of_data[middle_val] == target:
            return middle_val
        elif list_of_data[middle_val] < target:
            lower_bound = middle_val + 1
        elif list_of_data[middle_val] > target:
            upper_bound = middle_val - 1
    return -1


test_data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
tar = 15

print(binary_search(tar, test_data))