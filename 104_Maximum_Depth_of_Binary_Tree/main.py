# 定義二元樹節點類別
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# case 1 遞迴（DFS）
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 遞迴終止條件：如果節點為空，深度為 0
        if not root:
            return 0
        # 否則遞迴取得左右子樹的最大深度
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # 回傳較大的一邊 + 1（代表當前節點）
        return max(left_depth, right_depth) + 1

# case 2 BFS（層序遍歷）
from collections import deque


# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#
#         depth = 0
#         queue = deque([root])
#
#         while queue:
#             level_size = len(queue)
#             for _ in range(level_size):
#                 node = queue.popleft()
#                 if node.left: queue.append(node.left)
#                 if node.right: queue.append(node.right)
#             depth += 1
#
#         return depth

def test():
    solution = Solution()

    # 建立樹：[3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    assert solution.maxDepth(root1) == 3

    # 建立樹：[1,null,2]
    root2 = TreeNode(1)
    root2.right = TreeNode(2)

    assert solution.maxDepth(root2) == 2

    print("All tests passed!")

# 執行測試
if __name__ == "__main__":
    test()