class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target={}
        current={}
        window=len(s1)
        left=0
        if len(s1)>len(s2):
            return False

        for ch in s1:
            target[ch]=target.get(ch,0)+1
        
        for right in range(len(s2)):
            ch=s2[right]
            current[ch]=current.get(ch,0)+1
            if right-left+1>window:
                left_ch=s2[left]
                current[left_ch]-=1

                if current[left_ch]==0:
                    del current[left_ch]
                left+=1
            if current == target:
                return True
        return False





        # print(cur,tar)
        '''
        true-> s2 contains a permutation of s1 or false

        find the target freq of characters in s1

        fixed window problem: 
        window=len(s1)
        
         s1 -> "abc"
         target={a:1,b:1,c:1}

         s2-> "lecabee"
         two pointers:
         left=0
         target={a:1,b:1,c:1}
         right would in the for loop itereate till n
         l   e  c  a  b  e  e
         target={a:1,b:1,c:1}
      

         for right in s2:
            current[ch]=current.get(right,0)+1


            if right-left+1>window:
                left_ch=s2[left] 
                current[left_ch]-=1
                if current[left_ch]==0:
                    del current[left_ch]
                left+=1

            if current == target:
                return true

           current={l:1,e:2,c:1,a:1,b:1}
        
'''

