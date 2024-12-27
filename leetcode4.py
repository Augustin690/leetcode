"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))."""
from typing import List


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:

        m, n = len(nums1), len(nums2)
        merged_array = []
        read_index = 0
        if m >= n :
            for num1 in nums1:
                if read_index < len(nums2):
                    if num1 <= nums2[read_index]:
                        merged_array.append(num1)
                    else :
                        merged_array.append(nums2[read_index])
                        read_index +=1
                else:
                    merged_array.append(num1)
        else:
            for num2 in nums2:
                if read_index < len(nums1):
                    if num2 <= nums1[read_index]:
                        merged_array.append(num2)
                    else :
                        merged_array.append(nums1[read_index])
                        read_index +=1
                else:
                    merged_array.append(num2)

        #compute the median of merged array
        # odd length
        if len(merged_array) % 2 != 0 :
            median = merged_array[len(merged_array)//2]
        # even case
        else:
            median = (merged_array[len(merged_array)//2] + merged_array[len(merged_array)//2 - 1])/2

        return median


if __name__ == '__main__':

    nums1 = [1, 3]
    nums2 = [2]

    sol = Solution.findMedianSortedArrays(nums1, nums2)

    print(sol)