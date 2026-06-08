class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_str=""
        for i in strs:
            encoded_str= encoded_str+str(len(i))+"#"+i
            
        return encoded_str
        
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        # s = "5#Hello5#World"
        while i<len(s):
            j=i
            while(s[j]!="#"):
                j+=1
            length=int(s[i:j])

            word_start=j+1
            word_end=word_start+length

            res.append(s[word_start:word_end])

            i=word_end

        return res


