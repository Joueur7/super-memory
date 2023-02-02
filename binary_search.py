def linear_search(number_list, number_to_find):
    for index, elem in enumerate(number_list):
        if elem == number_to_find:
            return index
    return -1

def binary_serach(number_list, number_to_find):
    left = 0
    right = len(number_list) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        mid_number = number_list[mid]

        if mid_number == number_to_find:
            return mid

        if mid_number < number_to_find:
            left = mid + 1
        else:
            right = mid - 1

    return -1 

if __name__ == '__main__':
    number_list = [1, 2, 8, 12, 34, 56, 64, 67, 75, 98, 98, 102, 125]
    number_to_find = 75
    index = binary_serach(number_list, number_to_find)
    print(f"Number found at {index}")
