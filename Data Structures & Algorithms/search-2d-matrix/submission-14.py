class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])

        # converting to 1D matrix
        left=0
        right=rows*cols-1

        while left<=right:
            mid=(left+right)//2

            row=mid//cols # total number of rows passed
            col=mid%cols # cols passed in the current row

            value=matrix[row][col]
            if value==target:
                return True
            elif value<target:
                left=mid+1
            else:
                right=mid-1
        return False

