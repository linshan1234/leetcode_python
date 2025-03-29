class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 建立關括號的字典
        brackets_MAP = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []

        for char in s:
            # 如果是閉括號
            if char in brackets_MAP:
                element = stack.pop() if stack else "#"
                if brackets_MAP[char] != element:
                    return False

            # 如果是開括號
            else:
                stack.append(char)

        if len(s) > 1 and len(stack) == 0:
            return True
        else:
            return False


def test():
    solution = Solution()
    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("(]") == False
    assert solution.isValid("([])") == True
    print("All tests passed!")

# 執行測試
if __name__ == "__main__":
    test()
