# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # current row
        # current column
        left, right = 0, n
        top, bottom = 0, m

        # (0,0) -> (0,4) (1,4) -> (2,4), (2,3) -> (2,0), (1,0) -> (1,3)
        result = [[-1] * n for _ in range(m)]
        while head:
            # left to right
            for i in range(left, right):
                if head is None:
                    return result
                result[top][i] = head.val
                head = head.next
            top += 1
            # top to bottom
            for i in range(top, bottom):
                if head is None:
                    return result
                result[i][right - 1] = head.val
                head = head.next
            right -= 1

            # right to left
            for i in range(right - 1, left - 1, -1):
                if head is None:
                    return result
                result[bottom - 1][i] = head.val
                head = head.next
            bottom -= 1

            # bottom to top
            for i in range(bottom - 1, top - 1, -1):
                if head is None:
                    return result
                result[i][left] = head.val
                head = head.next
            left += 1

        return result
