def remove_even_integers_from_list(lst):
    return [num for num in lst if num % 2 != 0]

def merge_two_sorted_lists_1(lst1, lst2):
    result = []
    index_lst1 = 0
    index_lst2 = 0

    while index_lst1 < len(lst1) and index_lst2 < len(lst2):
        if lst1[index_lst1] < lst2[index_lst2]:
            result.append(lst1[index_lst1])
            index_lst1 += 1

        else:
            result.append(lst2[index_lst2])
            index_lst2 += 1

    while index_lst1 < len(lst1):
        result.append(lst1[index_lst1])
        index_lst1 += 1
    while index_lst2 < len(lst2):
        result.append(lst2[index_lst2])
        index_lst2 += 1
    return result

    # print(remove_even_integers_from_list([1,2,4,5,10,6,3]))

def merge_two_sorted_lists_2(lst1, lst2):
    index_lst1 = 0
    index_lst2 = 0
    while index_lst1 < len(lst1) and index_lst2 < len(lst2):
        if lst1[index_lst1] > lst2[index_lst2]:
            lst1.insert(index_lst1, lst2[index_lst2])
            index_lst2 += 1
        else:
            index_lst1 += 1
    while index_lst2 < len(lst2):
        lst1.append(lst2[index_lst2])
        index_lst2 += 1
    return lst1

def list_of_products_of_all_elements_1(lst):
    result = []
    left_multiplication = 1
    for index in range(len(lst)):
        right_multiplication = 1
        for item in lst[index+1:]:
            right_multiplication *= item
        result.append(right_multiplication * left_multiplication)
        left_multiplication = left_multiplication * lst[index]
    return result

def find_second_maximum(lst):
    first_max = float('-inf')
    second_max = float('-inf')
    for item in lst:
        if item > first_max:
            first_max = item
    for item in lst:
        if item > second_max and item < first_max:
            second_max = item
    return second_max

def find_second_maximum2(lst):
    first_max = float('-inf')
    second_max = float('-inf')
    for item in lst:
        if (item > first_max):
            second_max = first_max
            first_max = item
        if (item > second_max and item != first_max):
            second_max = item
    if (second_max == float('-inf')):
        return
    else:
        return second_max

print(find_second_maximum2([9, 2, 3, 6, 9]))
