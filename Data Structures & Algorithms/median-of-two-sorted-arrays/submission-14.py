class Solution:
    # TODO: Revisit. This one is a pain.
    # There exists a number which can partition both lists to create 2 equal length
    # sublists. We can test all possible i in the shorter list (A) such that A[i]
    # is equal to B[i] or between B[i+1] and B[i-1]
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = [nums1, nums2] if len(nums1) < len(nums2) else [nums2, nums1]
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2 # since len(B) > len(A), this won't error

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1