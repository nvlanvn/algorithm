# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        res = None
        curr = None
        while list1 and list2:
            val1 = list1.val
            val2 = list2.val

            if val1 > val2:
                node = ListNode(val2)
                list2 = list2.next
            else:
                node = ListNode(val1)
                list1 = list1.next
            if None == res:
                res = node
            else:
                if None == res.next:
                    res.next = node
                else:
                    curr.next = node
            curr = node
        while list2:
            val2 = list2.val
            node = ListNode(val2)
            curr.next = node
            curr = node
            list2 = list2.next
        while list1:
            val1 = list1.val
            node = ListNode(val1)
            curr.next = node
            curr = node
            list1 = list1.next

        return res
