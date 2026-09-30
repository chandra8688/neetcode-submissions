class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        current=[]
        def backtrack(start):
            if start==len(s):
                result.append(current.copy())
                return

            for i in range(start,len(s)):
                substring=s[start:i+1]

                if substring!=substring[::-1]:
                    continue
                current.append(substring)

                backtrack(i+1)

                current.pop()

        backtrack(0)
        return result