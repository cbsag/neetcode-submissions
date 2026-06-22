class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram_groups={}
        # for word in strs:
        #     # print(word)
        #     # print(self.ch_count(word))
        #     key="".join(sorted(word))
        #     print(key)
        #     if key not in anagram_groups:
        #         anagram_groups[key]=[]
        #     anagram_groups[key].append(word)
        #     # print(word,key)
        # # print(length,words)
        # result=list(anagram_groups.values())
        # return result


        anag={}
        for word in strs:
            key="".join(sorted(word))
            print(key)
            if key not in anag:
                anag[key]=[]
            anag[key].append(word)
        return list(sorted(anag.values()))