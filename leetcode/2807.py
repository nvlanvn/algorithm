# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while head and head.next:
            val1 = head.val
            val2 = head.next.val
            gcd_number = self.gcd(val1, val2)
            gcd_node = ListNode(gcd_number)
            tail.next = ListNode(val1, gcd_node)
            tail = gcd_node

            head = head.next

        if head:
            tail.next = ListNode(head.val)

        return dummy.next

    def gcd(self, val1, val2):
        if val2 == 0:
            return val1
        return self.gcd(val2, val1 % val2)
