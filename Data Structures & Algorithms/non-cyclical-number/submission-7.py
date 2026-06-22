class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        100
        '''
        # digit=str(n)
        seen = set()
        while n!= 1:
            if n in seen:
                return False
            seen.add(n)
            total=0
            for digit in str(n):
                print(digit)
                total += int(digit) ** 2
                print(total)
            n=total
        if n==1:
            return True