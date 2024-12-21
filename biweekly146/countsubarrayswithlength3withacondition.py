# Given an integer array nums, return the number of subarrays of length 3 such that the sum of the 
# first and third numbers equals exactly half of the second number.

# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def countSubarrays(self, nums) -> int:
        res = 0
        for i in range(0, len(nums)-2):
            if float(nums[i] + nums[i+2])== nums[i+1] / 2:

                res += 1

        return res