class Solution:
    def minWindow(self, s: str, t: str) -> str:

        
        target={}
        current={}
        left=0

        for ch in t:
            target[ch]=target.get(ch,0)+1
        
        need=len(target)
        have=0
        start=0
        left=0
        min_len=float("inf")

        for right in range(len(s)):
            ch=s[right]
            current[ch]=current.get(ch,0)+1

            if ch in target and current[ch]==target[ch]:
                have+=1
            while have==need:
                left_ch=s[left]
                current[left_ch]-=1
                length=right-left+1
                if length<min_len:
                    min_len=length
                    start=left

                if left_ch in target and current[left_ch]<target[left_ch]:
                    have-=1
                
    
                left+=1
                
        return "" if min_len == float("inf") else s[start:start+min_len]

        '''
        two strings s and t

        return shortest substring of s

            the shortest substring => every charcter in t with its duplicate is there in the substring 
            return if substring exist and empty if not
            

            edge cases is the substring can cotnain other letters as well if the belong in S and as long as all the valid windo contains the current count of charcters from string t
            privious we looked at exact count in current and target..
            
            so i go through string t and create the target count

            longest variable , 
            fint he minimun in the valid window..

            for ch in t:
                get the counts of each character:
            if len(s)<len(t):
                return ""
            for right in range(len(s)):
                ch=s[right]
                current[ch] get the count
        
            min_length=float("inf")
            need=len(target)
            have=0
                if ch in target and target[ch]==current[ch] :
                    have+=1
                while have==need:
                    length=right-left+1

                    if length<min_length:
                        min_lenth=length
                        start =left
                    left_ch=s[left]
                    current[left_ch]-=1
                    if left_ch in target and current[left_ch]<target[left_ch]:
                        have-=1
                    left+=1
            return "" if min_length == float("inf") else s[start:start+min_length]
            
        '''

        # target={}
        # current={}
        # for ch in t:
        #     target[ch]=target.get(ch,0)+1
        
        # start=0
        # need=len(target)
        # have=0
        # left=0
        # min_len=float("inf")

        # for right in range(len(s)):
        #     ch=s[right]
        #     current[ch]=current.get(ch,0)+1
        #     if ch in target and current[ch]==target[ch]:
        #         have+=1
            
        #     while have == need:
        #         length=right-left+1

        #         if length<min_len:
        #             min_len=length
        #             start=left
        #         left_ch=s[left]
        #         current[left_ch]-=1

        #         if left_ch in target and current[left_ch]<target[left_ch]:
        #             have-=1
        #         left+=1
        # return "" if min_len == float("inf") else s[start:start+min_len]

        