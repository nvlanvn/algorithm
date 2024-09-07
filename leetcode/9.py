class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = str(x)
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        return True
