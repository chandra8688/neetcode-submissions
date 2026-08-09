class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        need={}
        for ch in t:
            need[ch]=need.get(ch,0)+1
        window={}
        i=0
        have=0
        required=len(need)
        min_length=float("inf")
        start=0
        for j,ch in enumerate(s):
            if ch in need:
                window[ch]=window.get(ch,0)+1
                if window[ch]==need[ch]:
                    have+=1
            while have == required:
                current_window = j - i + 1
                
                if current_window<min_length:
                    min_length=current_window
                    start=i
                left_char=s[i]
                if left_char in need:
                    window[left_char]-=1
                    if window[left_char]<need[left_char]:
                        have-=1
                i+=1
        if min_length==float("inf"):
            return ""
        return s[start:start+min_length]





       
            
        