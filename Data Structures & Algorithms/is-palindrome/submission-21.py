class Solution:
    def isPalindrome(self, s: str) -> bool:
        sent= [char.lower() for char in s if char.isalnum()]
        clean_s= "".join(sent)
        reverse = "".join(clean_s[::-1])
        # print(clean_s,reverse)
        if clean_s == reverse:
            return True
        else:
            return False
            
        