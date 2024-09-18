class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1, n2):
            if str(n1) + str(n2) > str(n2) + str(n1):
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(compare))
        res = "".join(map(str, nums))
        if (int(res) <= 0):
            return "0"
        return res
