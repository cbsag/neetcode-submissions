class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target={}
        window_size=len(s1)
        for ch in s1:
            target[ch]=target.get(ch,0)+1
        
        left=0
        current={}

        for right in range(len(s2)):
            ch=s2[right]
            current[ch]=current.get(ch,0)+1

            if right-left+1>window_size:
                left_ch=s2[left]
                current[left_ch]-=1
                if current[left_ch]==0:
                    del current[left_ch]
                left+=1
            if current == target:
                return True
        return False
        
