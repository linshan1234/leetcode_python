# 正確的類別定義順序
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next


# 測試函數
def list_to_listnode(lst):
    """將 Python List 轉為 ListNode"""
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def listnode_to_list(node):
    """將 ListNode 轉回 Python List"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# 測試代碼
def test():
    solution = Solution()

    # 測試用例
    assert listnode_to_list(solution.mergeTwoLists(
        list_to_listnode([1, 2, 4]), list_to_listnode([1, 3, 4])
    )) == [1, 1, 2, 3, 4, 4]

    assert listnode_to_list(solution.mergeTwoLists(
        list_to_listnode([]), list_to_listnode([])
    )) == []

    assert listnode_to_list(solution.mergeTwoLists(
        list_to_listnode([]), list_to_listnode([0])
    )) == [0]

    print("✅ All tests passed!")


# 執行測試
if __name__ == "__main__":
    test()
