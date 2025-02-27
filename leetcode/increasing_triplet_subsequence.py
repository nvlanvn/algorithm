class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = float(inf)
        second_min = float(inf)
        for n in nums:
            if first_min >= n:
                first_min = n
            elif second_min >= n:
                second_min = n
            else:
                return True
        return False