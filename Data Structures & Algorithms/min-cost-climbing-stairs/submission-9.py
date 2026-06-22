class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stairs=len(cost)
        '''
        I need to check two approaches that is start at 0 and start at 1 index
        DP - problem
        '''
        dp= [0]* stairs
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range (2,stairs):
            dp[i]= cost[i] + min(dp[i-1],dp[i-2])
            print("step",i,"cost",cost[i])
        return min(dp[stairs-1],dp[stairs-2])

            
