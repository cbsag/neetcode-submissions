class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        time : O(n)
        space O(min(n,s size))
        sliding window pattern
        z   x   y   z   x   y   z"
                    l
                                r

        longest=1 -> 2 -> 3 
        seen= zxy -> xyz -> yzx -> zxy -> 
        '''
        longest=0
        left=0
        seen=set()

        for right in range(len(s)):
            ch=s[right]
            while ch in seen:
                seen.remove(s[left])
                left+=1
            seen.add(ch)
            longest=max(longest,right-left+1)
        return longest