class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        subset=[]
        def backtrack(i, remaining):
            if remaining==0:
                result.append(subset.copy())
                return
            if remaining <0 or i==len(nums):
                return
            subset.append(nums[i])
            backtrack(i, remaining-nums[i])

            subset.pop()

            backtrack(i+1, remaining)

        backtrack(0, target)
        return result