def search_insert_numbers(nums, target):

    index = 0

    while index < len(nums) and nums[index] < target:
        index += 1

    return index

list = [1, 2, 3]
target1 = 2
target2 = 4

print(search_insert_numbers(list, target1))
print(search_insert_numbers(list, target2))