from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()

        def clean_deque(i):
            if deque and deque[0] <= i-k:
                deque.popleft()  # remove numbers out of sliding window
            # remove numbers to the left and smaller than current index
            while deque and nums[deque[-1]] <= nums[i]:
                deque.pop()
            deque.append(i)

        for i in range(k):
            clean_deque(i)
        answ = [nums[deque[0]]]
        for i in range(k, len(nums)):
            clean_deque(i)
            answ.append(nums[deque[0]])
        return answ
