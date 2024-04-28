# You are given two integer arrays nums1 and nums2.

# From nums1 two elements have been removed, 
# and all other elements have been increased 
# (or decreased in the case of negative) by an integer, represented by 
# the variable x. As a result, nums1 becomes equal to nums2. 
# Two arrays are considered equal when they contain 
# the same integers with the same frequencies.
# Return the minimum possible integer x that achieves this equivalence.

# 3132
class Solution:
    def minimumAddedInteger(self, nums1, nums2):
        numsone, numstwo = sorted(nums1), sorted(nums2)
        l, r = 0, len(numstwo) - 1
        ret = 0
        while r < len(numsone):
            if numsone[l] - numstwo[0] == numsone[r] - numstwo[-1]:
                ret = min(ret, numstwo[0] - numsone[l])
                l += 1
                r += 1
            else:
                l += 1
                r += 1
        return ret