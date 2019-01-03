# https://www.interviewbit.com/problems/reverse-link-list-ii/

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        m = B
        n = C
        head = A
        if head == None or head.next == None:
            return head
        dummy = ListNode(0); dummy.next = head
        head1 = dummy
        for i in range(m - 1):
            head1 = head1.next
        p = head1.next
        for i in range(n - m):
            tmp = head1.next
            head1.next = p.next
            p.next = p.next.next
            head1.next.next = tmp
        return dummy.next
