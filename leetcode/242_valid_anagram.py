from collections import Counter


class Solution:
    def isAnagram_counter(self, s: str, t: str) -> bool:
        # Check length first - optimization
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
    

sol = Solution()
print(f"Counter: {sol.isAnagram_counter('anagram', 'nagaram')}") 