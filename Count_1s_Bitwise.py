class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            test = n%2
            if test == 1:
                count = count + 1
            n = int(n/2)
        return count
    def countBits(self, n: int) -> List[int]:
        listed = []
        for i in range(n+1):
            listed.append(self.hammingWeight(i))
        return listed

        
