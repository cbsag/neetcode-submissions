class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            print(num,"^",res)
            res= res ^ num
            print("result res",res)
        return res