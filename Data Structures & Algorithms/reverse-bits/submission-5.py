class Solution:
    def reverseBits(self, n: int) -> int:
        # result=0

        # for i in range(32):
        #     bit = n & 1
        #     result = result << 1
        #     result = result | bit
        #     n = n >> 1
        # return result

        
        res=0

        for i in range(32):
            
            bit = n & 1
            print(bit,n)
            res = res << 1
            print(res)
            res = res | bit
            print(res)
            n = n >> 1
        return res