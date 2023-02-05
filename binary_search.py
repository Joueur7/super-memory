def linear_search(number_list, number_to_find):
    for index, elem in enumerate(number_list):
        if elem == number_to_find:
            return index
    return -1

def binary_search(number_list, number_to_find):
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

def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


def binary_search_recursive(number_list, number_to_find, left, right):
    if right < left:
        return -1
    mid = (left + right) // 2
    if mid >= len(number_list) or mid < 0:
        return -1
    mid_number = number_list[mid]        
    
    if mid_number == number_to_find:
        return mid
            
    if mid_number < number_to_find:
        left = mid + 1
    else:
        right = mid - 1
    
    return binary_search_recursive(number_list, number_to_find, left, right)

if __name__ == '__main__':
    numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    index = binary_search_recursive(numbers_list, number_to_find, 0, len(number_list))
    print(f"Number found at {index}")
    indices = find_all_occurances(numbers_list, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")
