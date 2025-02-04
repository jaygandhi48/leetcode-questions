from typing import Optional

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root):
            """Find the leftmost node in the right subtree (inorder successor)."""
            while root.left:
                root = root.left
            return root

        if not root:
            return None

        if root.val == key:
            if not root.left and not root.right:  
                return None
            elif not root.right:  
                return root.left
            elif not root.left:  
                return root.right
            else:
                successor = findMin(root.right) 
                successor.right = self.deleteNode(root.right, successor.val)  
                successor.left = root.left
                return successor

        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)

        return root
