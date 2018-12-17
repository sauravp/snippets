# https://www.interviewbit.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        length = 0
        current = A
        while current is not None:
            current = current.next
            length += 1
        if B > length:
            B = B % length
            
        if B == 0:
            # no need to rotate
            return A
            
        k = length - B
        current = A
        for i in range(k-1):
            if current.next == None:
                current = A
            else:
                current = current.next
        end = current
        start = current.next if current.next is not None else A
        end.next = None
        current = start
        while current.next is not None:
            current = current.next
        current.next = A
        
        if start == end:
            start.next = None
            
        return start
