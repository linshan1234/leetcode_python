## 🚀 最佳解法：一次遍歷 (O(n))

### 🏆 **最佳策略：維護最低價格與最大利潤**

### 🧠 **思路：**
1. 使用 `min_price` 來記錄「當前最小的買入價格」。
2. 在遍歷每個 `prices[i]` 時：
    - 更新 `min_price` 為目前出現過的最小價格。
    - 計算 `profit = prices[i] - min_price`。
    - 如果 `profit > max_profit`，更新 `max_profit`。
3. 最後回傳 `max_profit`。
