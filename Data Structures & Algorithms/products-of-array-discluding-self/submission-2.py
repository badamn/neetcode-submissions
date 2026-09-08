class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                left[i] = left[i-1] * nums[i - 1]
                right[len(nums)-i-1] = nums[len(nums) - i] * right[len(nums) - i]
        return [left[i] * right[i] for i in range(len(nums))]
            