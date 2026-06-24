'''
s is a strings of uppercase character
choose upto K characters of the string and relace them to any string
atmost k characters and find the longest substring which contains one distint character
window_length-max_freq<=k
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # valid window = window_length - max_freq <= k
        # print(valid_window)
        
        # s = "AABA"
        # k = 1
        # A count=3
        # Bcount=1
        # window_length=4
        # maxfreq=3
        # replace_needed=4-3=1
        # then 1<=k (valid windown)


        left=0
        max_freq=0
        longest=0
        count={}
        for right in range(len(s)):
            ch=s[right]
            # print(ch)
            count[ch]=count.get(ch,0)+1
            # print(count)
            window=right-left+1
            max_freq=max(max_freq,count[ch])
            # print(ch,max_freq)
            # print("condition",window-max_freq,k)
            # print(count,"\n")
            if window-max_freq>k:
                count[s[left]]-=1
                left+=1
            longest=max(longest,right-left+1)
            # print(longest)
            # count[s[left]]-=1
            # if window-max_freq>k:
            
            # print(window)
        return longest


