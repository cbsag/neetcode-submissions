class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        #     # print(i,nums[i],len(nums))
        #     if i not in nums:
        #         return i
        # return 
        
        # true_sum=sum(range(len(nums)+1))
        # print(true_sum)

        # missing_sum=sum(nums)
        # print(missing_sum)

        # return true_sum - missing_sum


        real_sum=sum(range(len(nums)+1))
        missing_sum=sum(nums)
        return real_sum-missing_sum