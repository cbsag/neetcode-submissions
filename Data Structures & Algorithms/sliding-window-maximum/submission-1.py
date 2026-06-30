class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        brute force apparoch is to 
        left= 0
        res=[]
        
        for rigth in range(len(nums)):
            window = right-left+1

            if window>k:
                left+=1
                continue
            max_in_window=max(max_in_window,nums[right])


        '''
        res=[]
        for left in range(len(nums)-k+1):
            right=left+k
            window=nums[left:right]
            res.append(max(window))
        return res