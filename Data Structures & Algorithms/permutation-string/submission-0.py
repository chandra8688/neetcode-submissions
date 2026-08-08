class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq1={}
        freq2={}
        window_length=len(s1)
        
        for ch in s1:
            freq1[ch]=freq1.get(ch,0)+1
        for i in range(len(s1)):
            freq2[s2[i]]=freq2.get(s2[i],0)+1
        if freq1==freq2:
            return True
        for j in range(len(s1),len(s2)):
            freq2[s2[j]]=freq2.get(s2[j],0)+1
            left_char=s2[j-len(s1)]
            freq2[left_char]-=1

            if freq2[left_char]==0:
                del freq2[left_char]

            if freq1==freq2:
                return True
        return False
        

        