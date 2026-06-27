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
        cars=[]
        stack=[]
        for i in range(len(position)):
            time=(target-position[i])/speed[i]
            cars.append((position[i],time))

        cars.sort(reverse=True)
        for pos,time in cars:
            if not stack or  time >stack[-1]:
                stack.append(time)
        return len(stack)

