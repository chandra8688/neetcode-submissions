class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        subset=[]
        def backtrack(start,remaining):
            if remaining ==0:
                result.append(subset.copy())
                return
            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>remaining:
                    break
                subset.append(candidates[i])

                backtrack(i+1, remaining-candidates[i])
                subset.pop()

        backtrack(0,target)
        return result