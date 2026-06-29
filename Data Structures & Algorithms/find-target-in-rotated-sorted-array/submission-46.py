class Solution:
    def search(self, nums: List[int], target: int) -> int:


        '''
        nums=[3,4,5,6,1,2]
        mid=3
        target=1
        5 == 1:
        no

        5>1
        
        [3,4,5,6,1,2]
        5<1 -> right partion
        5>1 -> left partion
        elif :nums[mid]=5 <=target=1:
            right=mid-1
        else:
            left=mid+1
                '''

        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2

            if nums[mid]==target:
                return mid
            if nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1

        