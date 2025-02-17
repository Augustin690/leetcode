"""Construct Binary Tree from Preorder and Inorder Traversal.
Given two integer arrays preorder and inorder where preorder is
the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree."""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    #Time: O(N)
    #Space: O(N)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if inorder:

            root_val = preorder[0]
            tree = TreeNode(root_val)

            len_left_tree = inorder.index(root_val)

            left_inorder = inorder[:len_left_tree]
            right_inorder = inorder[len_left_tree + 1:]

            left_preorder = preorder[1: len_left_tree + 1]
            right_preorder = preorder[len_left_tree + 1:]

            tree.left = self.buildTree(left_preorder, left_inorder)
            tree.right = self.buildTree(right_preorder, right_inorder)

            return tree

    #time : O(N**2)  in the worst case because inorder.index() is  O(N) and it is called for each node.
    # space: O(N)
    # more elegant code
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if inorder:

            INDEX = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[INDEX])

            root.left = self.buildTree2(preorder, inorder[:INDEX])
            root.right = self.buildTree2(preorder, inorder[INDEX + 1:]
                                        )

            return root

    # optimized for time complexity by using hashmap
    # optimized for runtime buy using pointers instead of slicing inorder each time
    # Time: O(N) --> O(N) to build the hashmap, O(N) to build the tree
    # Space: O(N) --> O(N) to store hashmap, O(N) to store recursion stack
    def buildTree_hash(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a hashmap for quick index lookups
        inorder_index_map = {value: idx for idx, value in enumerate(inorder)}

        def helper(preorder, inorder_start, inorder_end):
            # Base case: if the range is invalid
            if inorder_start > inorder_end:
                return None

            # Get the root value and move the preorder pointer
            root_val = preorder.pop(0)
            root = TreeNode(root_val)

            # Get the index of the root value in the inorder traversal
            inorder_index = inorder_index_map[root_val]

            # Recursively build the left and right subtrees
            root.left = helper(preorder, inorder_start, inorder_index - 1)
            root.right = helper(preorder, inorder_index + 1, inorder_end)

            return root

        return helper(preorder, 0, len(inorder) - 1)
