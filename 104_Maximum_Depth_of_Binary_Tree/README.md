## 🧠 4. Thought Process 解題思路

### ✅ 方法一：遞迴（DFS）

- 使用 **深度優先搜尋（DFS）** 的遞迴方式解題。
- 每一層往下遞迴時，同時探索左子樹與右子樹的最大深度。
- 最後回傳：`max(左子樹深度, 右子樹深度) + 1`，代表包含當前節點的深度。

> **優點：**
> - 程式結構簡潔，易於理解。
> - 利用遞迴自然對應到樹的層次結構。

---

### ✅ 方法二：BFS（層序遍歷）

- 使用 **queue（佇列）** 實作廣度優先搜尋（Breadth-First Search）。
- 透過 `while` 迴圈遍歷每一層節點，並將下一層節點加入隊列。
- 每完成一層遍歷，深度加一，直到隊列為空。

> **優點：**
> - 可避免過深遞迴導致堆疊溢位（特別是在 Python 中）。
> - 可以同時計算各層的節點資訊（如平均值、最大值等）。

---

## 🚀 5. Optimal Solution Development 最佳解法發展

### 🔁 Step-by-Step 遞迴版本說明（DFS）

1. **Base Case**：如果節點為空（`None`），代表沒有深度，回傳 `0`
2. 遞迴取得左子樹與右子樹的最大深度：
   ```python
   left_depth = self.maxDepth(root.left)
   right_depth = self.maxDepth(root.right)
