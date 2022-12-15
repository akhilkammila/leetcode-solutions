import collections
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_counts = collections.defaultdict(int)
        l, r = 0, 0
        
        repeats = 0
        answ = 0
        while r < len(s):
            # slide r by 1
            if letter_counts[s[r]] == 1: repeats += 1
            letter_counts[s[r]] += 1
            r += 1

            # slide l until no repeats
            while repeats > 0:
                if letter_counts[s[l]]==2: repeats -= 1
                letter_counts[s[l]] -= 1
                l += 1
            answ = max(answ, r - l)
        return answ