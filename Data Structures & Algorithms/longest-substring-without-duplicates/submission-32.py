class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        left=0
        seen=set()
        for right in range(len(s)):
            ch=s[right]
            while ch in seen:
                seen.remove(s[left])
                left+=1
            seen.add(ch)
            longest=max(longest,len(seen))
        return longest
