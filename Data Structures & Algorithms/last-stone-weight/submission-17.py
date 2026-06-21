import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # print("Heapified list:", stones) 
        stones=[-stone for stone in stones]
        heapq.heapify(stones) 
        # print(stones)
        while len(stones)>1:
            first = -heapq.heappop(stones)
            # print(first)
            second = -heapq.heappop(stones)
            # print(second)
            if first>second:
                heapq.heappush(stones, -(first-second))
        if stones:
            return -stones[0]
            #     print(first-second)
            # # print(second)
        return 0