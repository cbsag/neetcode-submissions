class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target={}
        left=0
        window_size=len(s1)
        for ch in s1:
            target[ch]=target.get(ch,0)+1
        
        current_count={}
        for right in range(len(s2)):
            ch=s2[right]
            current_count[ch]=current_count.get(ch,0)+1
            if right-left+1>window_size:
                left_ch=s2[left]
                current_count[left_ch]-=1
                if current_count[left_ch]==0:
                    del current_count[left_ch]
                left+=1
            if current_count==target:
                return True
        return False



        
 
