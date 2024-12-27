"""Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory."""
from typing import List


class Solution:
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:


        # Length of the array
        n = len(nums)
        if n <= 2:
            return n  # If the array has 2 or fewer elements, all are valid.

        # Write index starts at 2 (allowing the first two elements by default)
        write_index = 2

        # Start from the third element and iterate
        for read_index in range(2, n):
            # Check if the current element is different from the element two positions back
            if nums[read_index] != nums[write_index - 2]:
                # Write the current element to the write_index position
                nums[write_index] = nums[read_index]
                write_index += 1

        # Return the number of valid elements
        return write_index

if __name__ == '__main__':

    nums = [0,0,1,1,1,1,2,3,3] #Input array
    expectedNums = [0,0,1,1,2,3,3] #The expected answer with correct length

    k = Solution.removeDuplicates(nums) # Calls your implementation

    assert k == len(expectedNums)

    for i in range(k) :
        assert nums[i] == expectedNums[i]
