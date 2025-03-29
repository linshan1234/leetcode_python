import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)

        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True

def test():
    solution = Solution()
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True
    assert solution.isPalindrome("race a car") == False
    assert solution.isPalindrome(" ") == True
    print("All tests passed!")

# 執行測試
if __name__ == "__main__":
    test()
