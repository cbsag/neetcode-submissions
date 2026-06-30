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
            max_in_window=max(max_in_whoindow,nums[right])


        '''
        # res=[]
        # for left in range(len(nums)-k+1):
        #     right=left+k
        #     window=nums[left:right]
        #     res.append(max(window))
        # return res

        l=r=0
        res=[]
        deque=collections.deque()

        while r<len(nums):
            # [1,2,1,0,4,2,6]
            while deque and nums[deque[-1]]<nums[r]:
                deque.pop()
            deque.append(r)
            # removed expired max 
            if l>deque[0]:
                deque.popleft()
            if(r+1)>=k:
                res.append(nums[deque[0]])
                l+=1
            r+=1
        return res

