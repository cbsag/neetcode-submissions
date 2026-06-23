class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # pairs={}
        # output=[]
        
        # for i in range(len(nums)):
        #     # print(i,len(nums))
        #     count=0
        #     if nums[i] not in pairs:
        #         count+=1
        #         pairs[nums[i]]=count
        #     else:
        #         count=pairs[nums[i]]
        #         pairs[nums[i]]=count+1
        # # print(pairs)
        # sorted_pairs=dict(sorted(pairs.items(),key=lambda x: x[1],reverse=True))
        # for key,value in sorted_pairs.items():
        #     output.append(key)
        #     if len(output)==k:
        #         break
        # return output
        freq={}
        count=0
        for num in nums:
            print(num)
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
        final=sorted(freq.items(),key=lambda x: x[1],reverse=True)
        res=[]
        for key,v in final[:k]:
            res.append(key)
        return res

