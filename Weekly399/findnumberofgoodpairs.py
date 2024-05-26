# You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

# A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

# Return the total number of good pairs.

class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        pairs = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                div = nums1[i] / (nums2[j] * k)
                if div.is_integer():
                    pairs.append([i, j])
        return len(pairs)
    
    