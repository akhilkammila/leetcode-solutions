from typing import List
import collections


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = collections.defaultdict(int)
        for i in range(len(s) - 9):
            sequences[s[i:i+10]] += 1

        output = []
        for string, count in sequences.items():
            if count > 1:
                output.append(string)
        return output
