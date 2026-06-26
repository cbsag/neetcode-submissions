class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # valid_window=window-max_freq <=k
        # Input: s = "XYYX", k = 2
        left=0
        count={}
        max_freq=0
        longest=0

        for right in range(len(s)):
            ch=s[right]
            count[ch]=count.get(ch,0)+1
            window=right-left+1
            max_freq=max(max_freq,count[ch])
            if window-max_freq>k:
                count[s[left]]-=1
                left+=1
            longest=max(longest,right-left+1)
        return longest








        

