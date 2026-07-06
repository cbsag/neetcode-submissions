# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        # print(root.val)
        self.dia=0
        def dfs(node):
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            self.dia=max(self.dia,left+right)
            return 1+max(left,right)
        dfs(root)
        return self.dia
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # self.diameter=0
        # def dfs(node):
        #     if not node:
        #         return 0
        #     left=dfs(node.left)
        #     right=dfs(node.right)
        #     self.diameter=max(self.diameter,left+right)
        #     return 1+max(left,right)
        # dfs(root)
        # return self.diameter






















        
        
        
        
        
        
        
        
        # self.dia=0
        # def depth(root):    
        #     if root is None:
        #         return 0
            
        #     left=depth(root.left)
        #     right=depth(root.right)
        #     self.dia=max(self.dia,left+right)
        #     return 1+max(left,right)
        # depth(root)
        # return self.dia