class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            test = n%2
            if test == 1:
                count = count + 1
            n = int(n/2)
        return count
