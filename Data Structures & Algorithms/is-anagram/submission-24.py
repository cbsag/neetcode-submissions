from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # built in lib
        # s_count = Counter(s)
        # t_count = Counter(t)
        # if len(s)!=len(t):
        #     return False
        # if s_count!=t_count:
        #     return False
        # else:
        #     return True
        
        # 
        # if len(s)!=len(t):
        #     return False
        
        # count={}
        # for char in s:
        #     # print(char)
        #     if char in count:
        #         count[char]+=1
        #     else:
        #         count[char]=1
        
        # for char in t:
        #     # print(char,count)
        #     if char not in count:
        #         return False
            
        #     count[char]-=1

        #     if count[char]<0:
        #         return False
        # return True
        
        if len(s)!=len(t):
            return False
        
        count={}
        
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1

        for ch in t:
            if ch not in count:
                return False
            
            count[ch]-=1

            if count[ch]<0:
                return False
        return True