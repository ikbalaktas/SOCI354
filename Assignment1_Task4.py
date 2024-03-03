def find_single_number(nums):

    result = 0

    for num in nums:
        result ^= num

    return result

list = [1, 1, 2, 3, 3, 4, 4]
print("The single number is: ", find_single_number(list))