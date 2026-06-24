class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        for i in range(len(s)):
            seen = set() 
            for j in range(i,len(s)):
                ch=s[j]
                if ch in seen:
                    break
                seen.add(ch)
            print("herer",seen)
            longest=max(longest,len(seen))
        return longest