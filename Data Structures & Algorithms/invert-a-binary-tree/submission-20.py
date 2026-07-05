# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr=root

        if root:
            curr_right=curr.right
            curr_left=curr.left

            curr.right=self.invertTree(curr_left)
            curr.left=self.invertTree(curr_right)

        return root





        































        # if not root:
        #     return None
        # new_root= TreeNode(root.val)
        # new_root.left=self.invertTree(root.right)
        # new_root.right=self.invertTree(root.left)

        # return new_root
        