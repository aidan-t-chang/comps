# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

# You are given an array of integers nums. 
# Return true if nums is a special array, otherwise, return false.

def isArraySpecial(nums):
    l, r = 0, 1
    while r < len(nums):
        if nums[l] % 2 == 0 and nums[r] % 2 == 0:
            return False
        elif nums[l] % 2 == 1 and nums[r] % 2 == 1:
            return False
        else:
            l += 1
            r += 1
    return True