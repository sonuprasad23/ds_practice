class Solution:

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        return count
# Example Usage 

sol = Solution()
print(sol.numJewelsInStones("aA", "aAAbbbb"))  # Output: 3
print(sol.numJewelsInStones("z", "ZZ"))  # Output: 0