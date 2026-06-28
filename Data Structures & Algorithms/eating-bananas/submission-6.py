class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # one_pile=ceil(pile/k)
        min=0
        
        left=1 # slowest speed
        right=max(piles) # fatestes ueful speed
        res=right #best valid speed so far
        # h is the total allwed hours
        while left<=right:
            k=(left+right)//2 # middle speed

            total_hours= 0
            for pile in piles:
                total_hours+=math.ceil(pile/k)

            if total_hours<=h:
                res=k
                right=k-1
            elif total_hours>h:
                left=k+1
        return res

