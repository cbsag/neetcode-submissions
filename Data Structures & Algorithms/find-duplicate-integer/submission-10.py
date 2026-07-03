class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen=set()

        # for num in nums:
        #     if num not in seen:
        #         seen.add(num)
        #     else:
        #         return num
        # space is O(n) andf time is O(n)

        # we want d it O(1)
        # what do we do next

        slow=fast=0   
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]

            if slow==fast:
                break
        slow=0
        while True:
            slow=nums[slow]
            fast=nums[fast]
            if slow==fast:
                return slow
                

        