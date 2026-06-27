class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # AOR = width * height
        # width = right-left-1

        stack=[]
        max_area=0
        n=len(heights)
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                bar=stack.pop()
                height=heights[bar]
                rb= i
                lb= stack[-1] if stack else -1
                width=rb-lb-1
                max_area=max(max_area,height*width)
            stack.append(i)
        while stack:
            bar=stack.pop()
            height=heights[bar]
            rb=len(heights)
            lb= stack[-1] if stack else -1
            width=rb-lb-1
            max_area=max(max_area,height*width)
        return max_area



            
