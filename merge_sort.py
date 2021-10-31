def merge_sorted_lists(list_a, list_b):
    list_a_length = len(list_a)
    list_b_length = len(list_b)
    # handle any empty lists
    if list_a_length == 0 and list_b_length > 0:
        return list_b
    elif list_a_length > 0 and list_b_length == 0:
        return list_a
    elif list_a_length == 0 and list_b_length == 0:
        return []
    
    a_index = 0
    b_index = 0

    merged_list = []

    # loops so long as there are elements in both lists
    while a_index < list_a_length and b_index < list_b_length:
        # if we have reached the end of list_a, we can append the remainder of list_b and return
        if a_index + 1 == list_a_length:
            merged_list += list_b[b_index:]
            return merged_list
        # if we have reached the end of list_b, we can append the remainder of list_a and return
        elif b_index + 1 == list_b_length:
            merged_list += list_a[a_index:]
            return merged_list
        elif list_a[a_index] < list_b[b_index]:
            merged_list.append(list_a[a_index])
            a_index += 1
        elif list_a[a_index] > list_b[b_index]:
            merged_list.append(list_b[b_index])
            b_index += 1
        # covers the case that both numbers are equal, we append both (order irrelevant)
        else:
            merged_list.append(list_a[a_index])
            a_index += 1
            merged_list.append(list_b[b_index])
            b_index += 1

    return merged_list

one = [1, 2, 4, 5]
two = [0,0,6]
three = [-30, -10, 0, 15, 16]
four = [-20, -5, 5]

test_1 = merge_sorted_lists(one, two)
test_2 = merge_sorted_lists(one, three)
test_3 = merge_sorted_lists(one, four)
test_4 = merge_sorted_lists(two, three)
test_5 = merge_sorted_lists(two, four)
test_6 = merge_sorted_lists(three, four)

print(test_1)
print(test_2)
print(test_3)
print(test_4)
print(test_5)
print(test_6)
