class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        i=0
        j=rows*cols-1
        while i<=j:
            mid=(i+j)//2
            row=mid//cols
            col=mid%cols
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                i=mid+1
            else:
                j=mid-1
        return False 
