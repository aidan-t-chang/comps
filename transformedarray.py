# You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:

# For each index i (where 0 <= i < nums.length), perform the following independent actions:
# If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
# If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
# If nums[i] == 0: Set result[i] to nums[i].
# Return the new array result.

# Note: Since nums is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end.


class Solution:
    def constructTransformedArray(self, nums):
        N = len(nums)

        res = []
        for i in range(N):
            if nums[i] > 0:
                res.append(nums[(i+nums[i])%N])
            elif nums[i] < 0:
                if i - abs(nums[i]) <= 0:
                    temp = abs(nums[i] + i)
                    res.append(nums[-1 * (temp%N)])
                else:
                    res.append(nums[(i+nums[i])])
            else:
                res.append(nums[i])

        return res