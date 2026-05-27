class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            # print(i,nums[i],len(nums))
            if i not in nums:
                return i
        return 