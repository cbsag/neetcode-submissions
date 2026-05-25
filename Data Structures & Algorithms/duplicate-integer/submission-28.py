class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dup_dict={}
        # for i in range(len(nums)):
            
        #     if nums[i] in dup_dict:
        #         return True
        #     else:
        #        dup_dict[nums[i]]=True
        #         # break
        # return False
        unique = set(nums)
        if len(unique)!=len(nums):
            return True
        else:
            return False
    