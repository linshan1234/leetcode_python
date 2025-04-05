## 📚 **1. Original Problem**

- **Original Problem Statement**

> Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
>
> Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

- **Question Translation (Traditional Chinese Translation)**

給定兩棵二元樹的根節點 `p` 和 `q`，請寫一個函式判斷這兩棵樹是否相同。

如果兩棵二元樹在**結構上相同**，且**每個對應節點的值也相同**，則認為它們是相同的。

---

## 🔎 **2. Problem Understanding**

- **Core Requirements and Constraints**
  - 兩棵樹完全相同才回傳 True。
  - 節點數不一定相同。
  - 樹可能為空（即 None）。

- **Identify Potential Challenges and Key Difficulties**
  - 必須正確處理 `None` 節點的比較。
  - 必須逐層遞迴確認所有節點都一致。
  - 注意不能只比記憶體位置，要比實際的值。

---

## 📊 **3. Visual Explanation**

### 經典例子 Tree Structure

```
Tree 1:         Tree 2:
    1               1
   / \             / \
  2   3           2   3
```

**Step-by-step:**
1. 比較根節點：1 == 1
2. 比較左子樹：2 == 2
3. 比較右子樹：3 == 3
→ 結果：True

---

## 🧠 **4. Thought Process**

### Solution 1: Recursive Comparison
- 遞迴方式逐層比較節點：值是否相同，左右子樹是否一致
- 優點：簡單明瞭，讀者易懂
- 缺點：有可能處理高深度樹時等速堆突

### Solution 2: Iterative with Stack/Queue
- 使用 BFS/DFS 算法，用 stack/queue 來代替通往
- 適合對話無法使用 recursion 的情境

**我們選擇 Solution 1 的原因：**
- 優先考慮簡單性和讀者容易理解
- Python 本身就很適合操作 recursion 形式

---

## 🚀 **5. Optimal Solution Development**

### 基礎思路
- 如果 p 和 q 均為 None，則 True
- 如果 p 或 q 其一為 None，則 False
- 如果 p.val != q.val，則 False
- 否則繼續檢查左右子樹

### 與其他方法比較
- 採用 DFS recursion 方式，比 BFS code 更簡潔
- 讓 code 更簡明，很適合 LeetCode 練習

---

## 📝 **6. Python Implementation**

```python
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        # 若兩個節點都為 None，則相同
        if not p and not q:
            return True
        # 若其中一個為 None 或值不同，則不同
        if not p or not q or p.val != q.val:
            return False
        # 遞迴比較左右子樹
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

---

## ⏱️ **7. Time and Space Complexity Analysis**

- **Time Complexity**: O(n)
  - n 為總節點數，所有節點都會被檢查一次

- **Space Complexity**: O(h)
  - h 為樹的高度
  - 最壯情況: O(log n)
  - 最壞情況 (假設 skewed tree): O(n)

---

## 🔎 **8. Optimization & Improvements**

- 如果在 recursion 中加入 memoization 對于部分可重用節點可以有效能
- 可以以 iterative BFS 方式實作
- 對大樹可考慮能限為香蕉帳的 DFS

**推薦練習**:
- 101. Symmetric Tree
- 572. Subtree of Another Tree
- 226. Invert Binary Tree

---

## 🧪 **9. Testing Strategy**

| Test Case | Input p | Input q | Expected | Description |
|-----------|---------|---------|----------|-------------|
| 1 | [1,2,3] | [1,2,3] | True | 一樣結構 |
| 2 | [1,2] | [1,null,2] | False | 結構不同 |
| 3 | [] | [] | True | 兩空樹 |
| 4 | [1,2,1] | [1,1,2] | False | 值不同 |

---

## 🌟 **10. In-Depth Understanding & Reflection**

- 學會了 binary tree 的 recursion 性質
- 加強對 tree traversal 的理解
- 在比較結構時不只檢查 reference，而是實際內容

**必備能力：**
- recursion 思維
- tree traversal 基礎
- 較差有總點與結構差異

