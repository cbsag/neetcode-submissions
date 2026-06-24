class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)-1):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             return[i+1,j+1]

        # because this is sorted lets use that to our advantage

        left = 0
        right = len(numbers)-1
        while left<right:
            total=numbers[left]+numbers[right]
            if total == target:
                return [left+1,right+1]
            elif total<target:
                left+=1
            
            else:
                right-=1