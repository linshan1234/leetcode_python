# 核心概念
走到第 n 階的方法數 = 走到第 n-1 階的方法 + 走到第 n-2 階的方法

這就是「斐波那契數列」的遞推關係

## Bottom-Up 動態規劃（Dynamic Programming）
使用一個 dp[] 陣列，從底部逐步建立每層的走法數量

每一階的走法為前兩階走法的總和

## 狀態轉移公式：

dp[i] = dp[i - 1] + dp[i - 2]
