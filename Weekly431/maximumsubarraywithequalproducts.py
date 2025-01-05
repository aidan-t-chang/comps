# You are given an array of positive integers nums.

# An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

# prod(arr) is the product of all elements of arr.
# gcd(arr) is the GCD of all elements of arr.
# lcm(arr) is the LCM of all elements of arr.
# Return the length of the longest product equivalent subarray of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.

# The term gcd(a, b) denotes the greatest common divisor of a and b.

# The term lcm(a, b) denotes the least common multiple of a and b.
import math

class Solution:
    def maxLength(self, nums) -> int:
        def prod(arr):
            re = 1
            for val in arr:
                re = re * val
            return re
        def gcd(arr):
            gcd = arr[0]
            for num in arr:
                gcd = math.gcd(gcd, num)
            return gcd
        def lcm_of_array(arr):
            lcm = arr[0]
            for num in arr:
                lcm = math.lcm(lcm, num)
            return lcm
            
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                # print(i, j)
                # print(nums[i:j+1])
                product = prod(nums[i:j+1])
                greatest = gcd(nums[i:j+1])
                lowest = lcm_of_array(nums[i:j+1])
                # print(product, greatest, lowest)
                if product == (greatest * lowest):
                    res = max(res, j - i + 1)
        return res