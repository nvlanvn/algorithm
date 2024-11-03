class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # remove redundant element
        total_num1 = len(nums1) - m
        total_num2 = len(nums2) - n

        for i in range(0, total_num1):
            nums1.pop()

        for i in range(0, total_num2):
            num2.pop()

        left_num1 = 0
        left_num2 = 0
        while True:
            # stop condition
            if left_num1 >= len(nums1) or left_num2 >= len(nums2):
                break
            # udate data
            if nums1[left_num1] > nums2[left_num2]:
                nums1.insert(left_num1, nums2[left_num2])
                left_num2 += 1
                left_num1 += 1
            else:
                left_num1 += 1

        while left_num2 < len(nums2):
            nums1.append(nums2[left_num2])
            left_num2 += 1
