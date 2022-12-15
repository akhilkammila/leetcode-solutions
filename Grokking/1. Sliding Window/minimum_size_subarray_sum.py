from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # if sum is >= target:
            # record answer
            # shift left
        # if sum is < target:
            # shift right

        l = 0
        total = 0
        answ = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                answ = min(answ, r - l + 1)
                total -= nums[l]
                l += 1
        return answ if answ!=float('inf') else 0