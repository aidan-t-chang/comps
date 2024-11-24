# You are given an integer array nums and two integers l and r. 
# Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is greater than 0.

# Return the minimum sum of such a subarray. If no such subarray exists, return -1.

# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def minimumSumSubarray(self, nums, l: int, r: int) -> int:
        res = float("inf")
        for right in range(l, r+1): 
            left = 0
            r = right
            while r <= len(nums):
                t = 0
                for n in nums[left:r]:
                    t += n
                if t > 0:
                    res = min(res, t)
                left += 1
                r += 1

        return -1 if res == float("inf") else res