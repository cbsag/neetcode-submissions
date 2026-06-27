class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        two array 
        one is position
        one is speed ... both of size n
        destination is at position target miles

        constraints : a car cannot padd another car ahead of it
        only catch up to the other car and drive at the same speed

        car-fleet is an non empty set of cars driving at same positon and same speed 

        '''
        # car_fleet=[]
        # Input: target = 10, position = [1,4], speed = [3,2]
        # 1->3(10-1)/3=3
        
        # 4->2(10-4)/2=3

        # each position check the time to target -> (taregt -position)/speed 
        # then sort them based on closer to target:
        # will have list of sorted time to taget from closer to farthest: this can be [()] list of tuples
        # (1,3)->3
        # (4,2)->3
        # car_fleet=0
        # position 4 time 3

        # position 1 time 3

        # current slowest fleet time ahead

        stack=[]
        car=[]
        print(position,target)
        for i in range(len(position)):
            time = (target-position[i])/speed[i]
            car.append((position[i],time))
        car.sort(reverse=True)
        print(car)

        for pos,time in car:
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)
        
            



