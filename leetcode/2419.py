class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_and = 0
        answer = 0
        ands = []

        for i, x in enumerate(nums):
            # print(max_and, answer, x)
            temp = []
            for a, idx in ands:
                new = a & x
                if not temp or new != temp[-1][0]:
                    if max_and < new:
                        max_and = new
                        answer = i - idx + 1

                    elif max_and == new:
                        answer = max(answer, i - idx + 1)

                    temp.append((new, idx))

            temp.append((x, i))
            ands = temp

            if max_and < x:
                max_and = x
                answer = 1

        return answer

