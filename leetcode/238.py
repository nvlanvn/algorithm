class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        for idx, val in enumerate(nums):
            if idx == 0:
                prefix.append(val)
            else:
                prefix.append(val * prefix[idx - 1])

        postfix = []
        for idx, val in enumerate(reversed(nums)):
            if idx == 0:
                postfix.append(val)
            else:
                postfix.append(val * postfix[idx - 1])

        postfix.reverse()
        for idx, val in enumerate(nums):
            if idx == 0:
                res.append(postfix[idx + 1])
            elif idx == len(nums) - 1:
                res.append(prefix[idx - 1])
            else:
                res.append(prefix[idx - 1] * postfix[idx + 1])
        return res
