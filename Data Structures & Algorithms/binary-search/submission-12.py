class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if target==nums[i]:
        #         return i
        # return -1
        for i in range(len(nums)):
            if target==nums[i]:
                return i
        return -1
            # return(i if target==nums[i] else -1)