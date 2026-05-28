class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        prices -> list of intergeres
        p[i] is the price of the coin on day i
            return the maximun profit you can achieve.
                I choose one day to buy a coin and different day in the future to sell i.
            I make not choose to make any transactiions where profi is 0



        '''
        # profit1=[]
        # max=0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         profit = prices[j]-prices[i]
        #         if max<profit:
        #             max=profit
        #             profit1.append(profit)
        # return max
        
        max=0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>max:
                    max=prices[j]-prices[i]
        return max


















