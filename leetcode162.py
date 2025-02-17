"""Find Peak Element"""

from typing import List


class Solution:

    @staticmethod
    # complexity in O(n), can do better
    def findPeakElement(self, nums: List[int]) -> int:
        index = len(nums)//2

        while 0 <= index < len(nums):
            # if we have 1 element, then its the peak.
            # otherwise, means that we started above 0 so if we arrived here it means we had
            # nums[0]> nums[1]  (every consecutive element is different)
            if index == 0 :
                return index

            elif nums[index] <= nums[index -1]:

                index = index - 1
            # if we are at the end of the list, and we have more than 1 element, it means we reached the peak
            # with the same reasoning as above
            elif index == len(nums) -1 :

                return index

            elif nums[index] <= nums[index +1]:

                index = index + 1

            else:

                return index

    def findPeakElement2(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            index = (left + right)//2
            # peak is in the left half, excluding index
            if nums[index] <= nums[index +1]:
                left = index + 1

            # peak is in the right half, including index
            else :
                right = index

        return left

if __name__ == '__main__':
    pass