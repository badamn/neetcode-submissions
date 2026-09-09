class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
            # Only start counting if num is the beginning
            # of a consecutive sequence.
            if num - 1 not in nums_set:
                cur = num
                cur_len = 1

                while cur + 1 in nums_set:
                    cur += 1
                    cur_len += 1

                max_len = max(max_len, cur_len)

        return max_len