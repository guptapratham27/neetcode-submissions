class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        final=defaultdict(list)

        for s in strs:

            l=[0]*26
            
            for i in range(len(s)):
                l[ord(s[i])-ord('a')]+=1
            final[tuple(l)].append(s)
        
        return list(final.values())

        