class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # AOR = width * height
        # width = right-left-1

        '''
        stack=indiies
        max_area
        while stack and height < height at top of the stack:
            pop bar
            get height of the bar
            lb is stack[-1] if stack else -1
            rb is i
            width = rb-lb-1
            area is max(max_area,height*width)
        while stack:
            pop bar
            get height of the bar
            rb=len(heights)
            same as the remaining things
        '''

        stack=[]
        max_area=0

        for i in range(len(heights)):
            while stack and heights[i]<=heights[stack[-1]]:
                bar=stack.pop()
                height=heights[bar]

                lb= stack[-1] if stack else -1
                rb=i
                width= rb-lb-1
                area=height*width
                max_area=max(max_area,area)
            stack.append(i)
        while stack:
            bar=stack.pop()
            height=heights[bar]
            lb=stack[-1] if stack else -1
            rb=len(heights)
            width=rb-lb-1
            area=width*height
            max_area=max(max_area,area)
        return max_area


            
