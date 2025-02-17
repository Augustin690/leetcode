"""Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level)."""
from typing import Optional, List



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # solution if binary tree was stored in a list
    @staticmethod
    def levelOrder_list(root: List) -> List[List[int]]:

        print(root)
        if len(root) == 0:
            return root

        # if node is at position i, left is at position  2i +1 and right 2i +2
        # level 0 has 1 node, lvl 1 has 2, lvl 2 has 4, lvl i has 2 ** i
        sol = []
        level = 0
        n_levels = 0
        i = 0
        while i < len(root):
            if i == 0:

                sol.append([root[i]])
                level += 1
                i += 1
            else:
                n_nodes = 2 ** level
                level_nodes = []
                for k in range(i, i+ n_nodes):
                    if root[k] != 'null':
                        level_nodes.append(root[k])

                sol.append(level_nodes)
                level += 1
                i+= n_nodes

        return sol

    # Streamlined version of previous solution
    # Time: O(N)
    # Space: O(N)
    def levelOrder_list2(root: List) -> List[List[int]]:
        if len(root) == 0:
            return []

        # Initialize variables
        result = []
        level = 0
        i = 0

        while i < len(root):
            # Number of nodes in the current level
            n_nodes = 2 ** level
            # Extract the current level's nodes
            level_nodes = root[i:i + n_nodes]
            # Filter out 'null' values
            level_nodes = [node for node in level_nodes if node != 'null']

            # Add non-empty levels to the result
            if level_nodes:
                result.append(level_nodes)

            # Move to the next level
            level += 1
            i += n_nodes

        return result

    # solution with some hints from chatgpt, inspired by BFS
    # time complexity: O(N), every node must be visited once to extract its value
    # space complexity: O(N), queue stores each level, at worst the last level contains N//2 nodes
    @staticmethod
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        # could've used collections.dequeue but list works as well
        q = [root]
        while len(q) > 0:
            current_level = []
            for _ in range(len(q)):
                # Dequeue from the front of the queue
                node = q.pop(0)
                current_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(current_level)

        return res

    # recursive solution, DFS. Less optimal, regarding storage, stack vs queue
    # Time: O(N) same as before
    # Space: O(log(N)) (stack) + O(N) (results list)
    def levelOrder_recursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        def solver(node: TreeNode, level: int):
            # Base case: if the node is None, do nothing
            if not node:
                return

            # Ensure the result list has a sublist for the current level
            if len(result) <= level:
                result.append([])

            # Add the current node's value to the appropriate level
            result[level].append(node.val)

            # Recursively process left and right children
            solver(node.left, level + 1)
            solver(node.right, level + 1)

        result = []  # Initialize the result list
        solver(root, 0)  # Start recursion from the root at level 0
        return result


if __name__ == '__main__':

    root = [3, 9, 20, 'null', 'null', 15, 7]

    print(Solution().levelOrder_list(root))
