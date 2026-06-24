class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        area = width* height
        I choose 2 bar and find the maximun amount of water a container can store.
        move the pointer with the shortest height and see the area 
        left=0
        right=end
        wdith = right - left
        height=min(left,right)
        area= width*height
        max_area=area
        '''

        left=0
        right = len(heights)-1
        max_area=0

        while left<right:
            width = right-left
            height=min(heights[right],heights[left])
            area=width*height
            max_area=max(max_area,area)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_area