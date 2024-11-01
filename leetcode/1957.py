class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        left = 0
        right = len(s)
        while left < right:
            next_idx = left + 1
            char = s[left]
            while next_idx < right and char == s[next_idx]:
                next_idx += 1
            if left + 1 == next_idx:
                res.append(s[left])
                left += 1
            else:
                res.append(s[left] * 2)
                left = next_idx
        return "".join(res)
