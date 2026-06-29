class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        brute force approach is to merge both and sort them

        if even % len and odd mid//len
        '''

        merge=nums1+nums2
        merge.sort()
        print(merge)
        n= len(merge)
        median=0
        if len(merge)%2!=0:
            median=merge[n//2]
        else:
            median=(merge[n//2-1]  +   merge[n//2]) /2
        return median