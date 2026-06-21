class Solution:
    def climbStairs(self, n: int) -> int:
        # if n==1:
        #     return 1
        # if n==2:
        #     return 2
        # one_s=2
        # two_s=1

        # for i in range(3,n+1):
        #     current_s = one_s+ two_s
        #     two_s=one_s
        #     one_s=current_s
        # return one_s
        if n == 1 or n == 2:
            return n

        one_s = 1
        two_s = 2

        for i in range(3, n + 1):
            curr = one_s + two_s
            one_s = two_s
            two_s = curr
        return two_s
        

        
        