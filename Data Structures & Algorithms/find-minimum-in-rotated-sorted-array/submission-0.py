class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        array was sorted and then rotated n times
        so we ussualy do left=0
        right=len(nums)-1
        mid=(left+right)//2
        then chekc target..

        nums[mid]>nums[right] min is on the right 
        nums[mid]<=nums[left] mid or left side

        nums = [4,5,6,7,0,1,2]
        nums=  [0,1,2,3,4,5,6]
        left = 0

        right = 6
        while(left<right):
        mid = 3
        nums[mid]>num[right]
            left=mid+1
        nums[mid]<=nums[left]
            right=mid
        return nums[left]
        '''
        left=0
        right=len(nums)-1

        while(left<right):
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            elif nums[mid]<=nums[right]:
                right=mid
        return nums[left]
        