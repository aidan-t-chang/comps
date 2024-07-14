# You are given an array of integers nums and the head of a linked list. 
# Return the head of the modified linked list after removing all nodes from 
# the linked list that have a value that exists in nums.



''''

NON FUNCTIONAL SOLUTION. very mad.

'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums, head):
        if head.val in nums:
            head = head.next
        if not head:
            return head
        l, r = head, head.next
        while r:
            while l.val in nums:
                head = r
                l = r
                r = r.next
            while r and r.val in nums:
                r = r.next
            l.next = r
            l = r
            if r:
                r = r.next
        return head