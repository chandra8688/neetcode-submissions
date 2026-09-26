class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        subset=[]
        used=[False]*len(nums)
        def backtrack():
            if len(subset)==len(nums):
                result.append(subset.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue

                subset.append(nums[i])
                used[i]=True

                backtrack()

                subset.pop()
                used[i]=False
        backtrack()
        return result