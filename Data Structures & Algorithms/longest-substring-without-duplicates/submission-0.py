class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        chars=set()
        max_length=0
        for j,ch in enumerate(s):
            while ch in chars:
                chars.remove(s[i])
                i+=1
            chars.add(ch)
            max_length=max(max_length,j-i+1)
        return max_length
        