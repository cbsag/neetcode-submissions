class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])

        # fake 1d matrix
        left=0
        right=rows*cols-1

        while left<=right:
            mid=(left+right)//2
            row=mid//cols # this give sme the total number of rows passed
            col=mid%cols # this gives the leftover columns int eh current row
            value=matrix[row][col]
            if value ==target:
                return True
            elif value<target:
                left=mid+1
            else:
                right=mid-1
        return False