class Solution:
    def hammingWeight(self, n: int) -> int:
        # # digits=[int(char) for char in str(n)]
        # count =0

        # while n:
        #     if n& 1 == 1:
        #         count+=1
        #     n=n >>1
        # return count
        count=0
        binary = bin(n)
        for ch in binary:
            if ch in binary:
                if ch=="1":
                    count+=1
        return count

