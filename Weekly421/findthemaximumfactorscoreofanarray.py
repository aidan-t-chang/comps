# You are given an integer array nums.

# The factor score of an array is defined as the product of the LCM and GCD of all elements of that array.

# Return the maximum factor score of nums after removing at most one element from it.

# Note that both the LCM and GCD of a single number are the number itself, and the factor score of an empty array is 0.

# The term lcm(a, b) denotes the least common multiple of a and b.

# The term gcd(a, b) denotes the greatest common divisor of a and b

# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
from math import gcd
from functools import reduce

class Solution:
    def maxScore(self, nums) -> int:
        def lcm(a, b): 
            return (a * b) // gcd(a, b)

        def gcd1(a, b):
            while b:
                a, b = b, a % b
            return a 

        def gcd2(arr):
            if not arr:
                return 0

            curr = arr[0]
            for num in arr[1:]:
                curr = gcd(curr, num)

            return curr
            
        def compute_lcm(arr):
            return reduce(lcm, arr)

        n = len(nums)

        if n == 0:
            return 0

        big_gcd = gcd2(nums)
        big_lcm = compute_lcm(nums)

        score = big_gcd * big_lcm

        for i in range(n):
            new_array = nums[:i] + nums[i+1:]

            if new_array:
                newg = gcd2(new_array)
                newl = compute_lcm(new_array)
                score = max(score, newg * newl)

        return score