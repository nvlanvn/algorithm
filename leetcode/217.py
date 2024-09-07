class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_nums = {}
        for i in nums:
            if hash_nums.get(i) != None:
                return True
            hash_nums.update({i: i})
        return False
