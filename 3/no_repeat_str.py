class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if not s:
            return 0
        if n<2:
            return 1
        i,j=0,0
        d=dict()
        maxlen=0
        while i<n and j<n:
            if s[j] in d:
                i=d[s[j]]+1 if i<d[s[j]]+1 else i
            maxlen=max(maxlen,j-i+1)
            d[s[j]]=j
            j+=1
        return maxlen