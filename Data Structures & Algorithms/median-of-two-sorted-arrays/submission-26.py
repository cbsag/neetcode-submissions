class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        brute force approach is to merge both and sort them

        if even % len and odd mid//len
        '''

        # merge=nums1+nums2
        # merge.sort()
        # print(merge)
        # n= len(merge)
        # median=0
        # if len(merge)%2!=0:
        #     median=merge[n//2]
        # else:
        #     median=(merge[n//2-1]  +   merge[n//2]) /2
        # return median
        # time O(m+n log m+n ) sorting
        # space is O(m+n) merge array

        '''
        A [ .. | leftA|rightA ]
        B [.. | LeftB | rigthB]
        '''
        A,B=nums1,nums2
        # B=num2
        # we need to run the binary search on the smaller one so A will aleaye be the smallest array
        total = len(nums1)+len(nums2)
        half=total//2
        if len(B)<len(A):
            A,B=B,A

        # Binary search on A (the smallest)

        l,r=0,len(A)-1

        while True:
            i=(l+r)//2 # A 
            j = half-i - 2 # j is the index so i as one 0 and j as 0 so -2

            leftA=A[i] if i>=0 else float("-inf")
            rightA=A[i+1]  if (i+1) <len(A) else float("inf")
            leftB=B[j] if j>=0 else float("-inf")
            rightB=B[j+1] if (j+1) <len(B) else float("inf")

            # partion is correct
            if leftA<=rightB and leftB <=rightA:
                # odd
                if total % 2:
                    return min(rightA,rightB)
                #even
                return (max(leftA,leftB) + min(rightA,rightB)) /2
            elif leftA>rightB:
                r=i-1
            else:
                l=i+1
        