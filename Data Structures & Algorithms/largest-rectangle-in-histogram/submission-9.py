class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        heights: 
        '''
        stack=[]
        max_area=0
        # [7,1,7,2,2,4]
        # [0]
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                tall=stack.pop()
                if stack:
                    left_bound=stack[-1]
                else:
                    left_bound=-1
                height=heights[tall]
                right_bound=i
                width=right_bound-left_bound-1
                print("i at hw ->",i,height,width)
                area=width*height
                print("area",area)
                max_area=max(max_area,area)

            stack.append(i) 
        while stack:
            tall=stack.pop()
            height=heights[tall]
            right_bound=len(heights)
            left_bound= stack[-1] if stack else -1
            width=right_bound-left_bound-1
            area=width*height 

            max_area=max(max_area,area)
        return max_area