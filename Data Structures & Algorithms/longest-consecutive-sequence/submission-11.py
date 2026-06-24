class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq=set(nums)
        # print(seq)
        longest=0
        for num in seq:
            # print(num,num-1)
            if num-1 not in seq:
                current=num
                current_len=1
                # print("start",current)
                while current+1 in seq:
                    current+=1
                    current_len+=1
                # print(longest,current_len)
                longest= max(longest,current_len)
                # print("count",longest)
        return longest

        
        