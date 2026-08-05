class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        left_max=height[i]
        right_max=height[j]
        total=0
        while i<j:    
            if left_max<right_max:
                i+=1
                if height[i]>=left_max:
                    left_max=height[i]
                else:
                    total+=left_max-height[i]
            else:
                j-=1
                if height[j]>=right_max:
                    right_max=height[j]
                else:
                    total+=right_max-height[j]
        return total