class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        i = 0
        j = m

        while i <= j:

            partition1 = (i + j) // 2
            partition2 = (m + n + 1) // 2 - partition1

            if partition1 == 0:
                i1 = float("-inf")
            else:
                i1 = nums1[partition1 - 1]

            if partition1 == m:
                j1 = float("inf")
            else:
                j1 = nums1[partition1]

            if partition2 == 0:
                i2 = float("-inf")
            else:
                i2 = nums2[partition2 - 1]

            if partition2 == n:
                j2 = float("inf")
            else:
                j2 = nums2[partition2]

            # Correct partition
            if i1 <= j2 and i2 <= j1:

                # Odd
                if (m + n) % 2:
                    return max(i1, i2)

                # Even
                return (max(i1, i2) + min(j1, j2)) / 2

            # Too many elements taken from nums1
            elif i1 > j2:
                j = partition1 - 1

            # Too few elements taken from nums1
            else:
                i = partition1 + 1

        return 0.0