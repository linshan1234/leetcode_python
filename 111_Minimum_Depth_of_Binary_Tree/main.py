# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        if root.left != None and root.right == None:
            return 1 + self.minDepth(root.left)
        elif root.left == None and root.right != None:
            return 1 + self.minDepth(root.right)
        else:
            return 1 + min(self.minDepth(root.right), self.minDepth(root.left))


def test():
    solution = Solution()

    # 建立樹：[3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    assert solution.minDepth(root1) == 2

    # 建立樹：[1,null,2]
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(4)
    root2.right.right.right = TreeNode(5)
    root2.right.right.right.right = TreeNode(6)

    assert solution.minDepth(root2) == 5

    print("All tests passed!")

# 執行測試
if __name__ == "__main__":
    test()