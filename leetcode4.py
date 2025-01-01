"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log(m+n))."""

from typing import List


class Solution:

    # O(Nlog(N)) time complexity, O(N) space complexity, naive suboptimal approach, but few lines of code
    # Very fast runtime (0 ms), beats 100% on Leetcode. Memory: 18.11 MB, beats only 8 %
    @staticmethod
    def findMedianSortedArrays(list1: List[int], list2: List[int]) -> float:

        # storing a list, memory inefficient compared to the pointer approach
        merged = sorted(list1 + list2)

        #compute the median of merged array
        # odd length
        if len(merged) % 2 != 0 :
            median = merged[len(merged)//2]
        # even length
        else:
            median = (merged[len(merged)//2] + merged[len(merged)//2 - 1])/2

        return median

    """https://leetcode.com/problems/median-of-two-sorted-arrays/editorial """
    # merge and sort approach: get the k-th (k+1 if m+n is even) smallest integer of the merged lists --> median
    # do not need to consider the elements after the median since the 2 arrays are already sorted
    # time complexity: O(n + m) Space complexity: O(1).
    # Runtime: 5 ms,  beats 24%. Memory: 18.3 MB, beats 8 %
    @staticmethod
    def mergeSort(
            self, nums1: List[int], nums2: List[int]
    ) -> float:
        m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0

        # Get the smaller value between nums1[p1] and nums2[p2].
        def get_min():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans

        if (m + n) % 2 == 0:
            for _ in range((m + n) // 2 - 1):
                _ = get_min()
            # (m + n) nth and (m+n+ 1) smallest element/2
            return (get_min() + get_min()) / 2

        # m + n is odd, so we repeat the search m+n//2 + 1 times to get the median element
        else:
            for _ in range((m + n) // 2):
                _ = get_min()
            return get_min()

    # Recursive binary search, to achieve logarithmic time limit
    # We search the k-th (and k + 1 if even length) element using binary search-like algorithm
    # Time complexity: O(log(m * n)) Space complexity: O(log(m * n)) recursion steps. O(1) if tail call optim applied.
    # Runtime: 7 ms, beats 18% Memory: 19.08 MB, beats 8%
    @staticmethod
    def binSearch(
            A: List[int], B: List[int]
    ) -> float:

            na, nb = len(A), len(B)
            n = na + nb

            def solve(k, a_start, a_end, b_start, b_end):
                # If the segment of on array is empty, it means we have passed all
                # its element, just return the corresponding element in the other array.
                if a_start > a_end:
                    return B[k - a_start]
                if b_start > b_end:
                    return A[k - b_start]

                # Get the middle indexes and middle values of A and B.
                a_index, b_index = (a_start + a_end) // 2, (b_start + b_end) // 2
                a_value, b_value = A[a_index], B[b_index]

                # If k is in the right half of A + B, remove the smaller left half.
                if a_index + b_index < k:
                    if a_value > b_value:
                        return solve(k, a_start, a_end, b_index + 1, b_end)
                    else:
                        return solve(k, a_index + 1, a_end, b_start, b_end)
                # Otherwise, remove the larger right half.
                else:
                    if a_value > b_value:
                        return solve(k, a_start, a_index - 1, b_start, b_end)
                    else:
                        return solve(k, a_start, a_end, b_start, b_index - 1)

            if n % 2:
                return solve(n // 2, 0, na - 1, 0, nb - 1)
            else:
                return (
                        solve(n // 2 - 1, 0, na - 1, 0, nb - 1)
                        + solve(n // 2, 0, na - 1, 0, nb - 1)
                ) / 2


    # Better binary search: performing the binary search only on the smaller array of nums1 and nums2, thus the time complexity is reduced to O(log(min(m,n))).
    #
    @staticmethod
    def binSearch2( A: List[int], B: List[int]) -> float:
        pass
if __name__ == '__main__':

    nums1 = [1, 3]
    nums2 = [2]

    sol = Solution.findMedianSortedArrays(nums1, nums2)

    print(sol)