class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        for left, right in queries:
            total = arr[right]
            remove = 0 if left == 0 else arr[left - 1]
            res.append(total ^ remove)
        return res

