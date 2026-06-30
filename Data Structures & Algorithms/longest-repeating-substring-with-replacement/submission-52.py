class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # valid_window=window-max_freq <=k
        # Input: s = "XYYX", k = 2

        longest=0
        count={}
        left=0
        max_freq=0

        for right in range(len(s)):
            ch=s[right]
            count[ch]=count.get(ch,0)+1
            window=right-left+1
            # print(window,count)
            max_freq=max(max_freq,count[ch])

            replacement=window-max_freq
            print(count,window,max_freq,replacement)
            if replacement>k:
                count[s[left]]-=1
                left+=1
            longest=max(longest,right-left+1)
        return longest



            







        

