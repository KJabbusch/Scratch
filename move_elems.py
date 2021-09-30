def rotate_list(list_name, shift_by):
    if shift_by % len(list_name) == 0:
        return list_name
    elif len(list_name) < shift_by:
        shift_by = shift_by % len(list_name)
    
    for x in range(shift_by):
        last = list_name[-1]
        list_name.insert(0, last)
        list_name.pop()
    return list_name

sample_list = [1, 2, 3, 4, 5]
print(rotate_list(sample_list, 199))

def skyline(building_list):
    viewable = []
    for x in range(1, len(building_list)):
        current_building = building_list[x-1]
        next_building = building_list[x]

        if 0 < current_building <= next_building:
            viewable.append(current_building)
        elif

    return viewable

okay = [-1, 1, 3, 7, 7, 3]
print(skyline(okay))