"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log(m+n))."""
from math import inf
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
    # merge and sort approach: get the k-th (k+1 if m+n is even) smallest integer of the merged lists --> median, where k
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
            # average of (m + n)/2 nth and (m+n)/2 + 1 smallest element
            return (get_min() + get_min()) / 2

        # m + n is odd, median is (m+n+1)/2 th smallest element
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

            # k depends on whether total length na + nb is odd or even
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

            # total length is odd, k = n //2, same as n/2 + 1 th element bc index starts at 0 in Python
            if n % 2:
                return solve(n // 2, 0, na - 1, 0, nb - 1)
            # total length is even, average k-th and k+1-th elements where k = n//2 - 1
            # same as averaging n/2th and n/2 + 1 - th elements, bc index start at 0 in Python
            else:
                return (
                        solve(n // 2 - 1, 0, na - 1, 0, nb - 1)
                        + solve(n // 2, 0, na - 1, 0, nb - 1)
                ) / 2


    # Better binary search: performing the binary search only on the smaller array of nums1 and nums2, thus the time complexity is reduced to O(log(min(m,n))).
    # Time complexity: O(log(m + n)) Space complexity:
    @staticmethod
    def binSearch2( A: List[int], B: List[int]) -> float:

        n, m = len(A), len(B)

        # if B is the smaller array, swap the arrays
        if m < n:
            A,B = B,A
            n, m = m,n

        def solve(left, right):
            maxLeftA = 0
            minRightB = 0

            while left < right:

                partitionA = (left + right) //2
                partitionB = (m+ n)//2 - partitionA
                # by construction, the smaller half partitionA + partitionB contains (m+n+1)/2 elements
                # remember that the target value index depends on whether m+n is odd or even
                # odd: find (m+m+1)/2 = (m + n) //2 + 1 th smallest element even: average (m+n)/2 and (m+n)/2 + 1 elements
                if partitionA < 1 :
                    maxLeftA = float(-inf)
                else:
                    maxLeftA = A[partitionA - 1]
                if partitionA >= n :
                    minRightA = float(inf)
                else:
                    minRightA = A[partitionA]

                if partitionB < 1 :
                    maxLeftB = float(-inf)
                else:
                    maxLeftB = A[partitionA - 1]
                if partitionB >= m :
                    minRightB = float(inf)
                else:
                    minRightB = A[partitionA]

                if maxLeftA > minRightB:
                    # maxLeftA is too large to be in the smaller half,  we should look for a smaller partition value of A
                    #maxleftA should be in larger halff
                    right = partitionA - 1
                elif maxLeftB > minRightA:
                    # we are too far on the left side for partitionA, we should look for a larger partition value of A
                    # minRightA should be in smaller half
                    left = partitionA + 1
                else:
                    return maxLeftA, minRightA, maxLeftB, minRightB

        maxLeftA, minRightA, maxLeftB, minRightB = solve(0, n)
        # odd case, we search for (m + n)//2 + 1 th element
        if (n+m) % 2:
            # median is the max value of the smaller half
            return max(maxLeftA, maxLeftB)

        # even case, average (m + n)/2 and  (m + n)/2 + 1 elements
        else:
            # average max value of smaller half and min value of larger half
            return (max(maxLeftA, maxLeftB) + min(minRightB, minRightA)) /2


if __name__ == '__main__':

    nums1 = [1, 3, 4]
    nums2 = [2, 5]

    sol = Solution.binSearch2(nums1, nums2)

    print(sol)