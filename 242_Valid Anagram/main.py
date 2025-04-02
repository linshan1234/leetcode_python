class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = [0] * 26  # a~z 26個英文字母

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        # 如果是異位詞，每個值應該都是 0
        for c in count:
            if c != 0:
                return False

        return True



def test():
    solution = Solution()
    assert solution.isAnagram("anagram", "nagaram") == True
    assert solution.isAnagram("rat", "car") == False
    assert solution.isAnagram("a","a") == True
    assert solution.isAnagram("abc","abcd") == False
    assert solution.isAnagram("abac","baca") == True
    assert solution.isAnagram("a"*50000, "a"*49999 + "b") == False
    print("All tests passed!")

# 執行測試
if __name__ == "__main__":
    test()