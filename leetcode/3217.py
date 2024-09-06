# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = None
        curr = None
        nums_hash = {num: num for num in nums}
        while head:
            val = head.val
            if not nums_hash.get(val):
                node = ListNode(val)
                if None == res:
                    res = ListNode(val)
                else:
                    if None == res.next:
                        res.next = node
                        curr = node
                    else:
                        curr.next = node
                        curr = node
            head = head.next
        return res
