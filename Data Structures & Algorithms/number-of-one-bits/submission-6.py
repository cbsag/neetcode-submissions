class Solution:
    def hammingWeight(self, n: int) -> int:
        # digits=[int(char) for char in str(n)]
        count =0

        while n:
            if n& 1 == 1:
                count+=1
            n=n >>1
        return count
        