class Solution:
    def countBits(self, n: int) -> List[int]:
        # # binary=bin(n)
        # output=[]
        # for i in range(0,n+1):
        #     count=0
        #     binary=bin(i).count("1")
        #     output.append(binary)
        # return output
        output=[]
        for i in range(n+1):
            count=0
            binary=bin(i).count("1")
            print(binary)
            output.append(binary)
        return output