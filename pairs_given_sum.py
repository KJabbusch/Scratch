# gets rid of any integers larger than "sum" we are looking for
def binary_search(num_list):
    low = 0
    high = len(num_list) - 1

    while low <= high:
        mid = low + ((high-low)//2)

        if sum_num < num_list[mid]:
            high = mid - 1
        else:
            low = mid + 1

        if num_list[mid] < sum_num:
            return num_list[:mid]
    return None

# gets rid of large numbers if the sum of the smallest int > "sum" we are looking for
def shorten_numlist(nums):
    while (nums[0] + nums[-1]) > sum_num:
        nums.pop()
    return nums

def find_sum_pairs(nums):
    if len(nums) <= 1:
        return None
    nums = sorted(nums)
    binary_search(nums)
    shorten_numlist(nums)

    nums_copy = nums[:]
    counter_dict = {}
    i = 0
    
    for num in nums:
        num_to_find = sum_num - (nums_copy[-1])
        if num > num_to_find:
            nums_copy.pop()
        if num in nums_copy and nums_copy[-1] + num == 21:
            counter_dict[(nums_copy[-1], num)] = 1
        
    return len(counter_dict)

my_nums = [20, 1, 19, 2, 18, 3, 21, 0, 25, 3, 8]
sum_num = 21

print(find_sum_pairs(my_nums))
