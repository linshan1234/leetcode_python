# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head

        while curr:
            next_temp = curr.next  # 暫存下一個節點
            curr.next = prev       # 反轉指向
            prev = curr            # prev 向前移
            curr = next_temp       # curr 向前移

        return prev  # prev 是新的頭


# 🔧 工具函式：將 Python list 轉為 linked list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# 🔧 工具函式：將 linked list 轉為 Python list（方便檢查結果）
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# 🧪 主測試區
if __name__ == "__main__":
    # 建立 linked list: 1 → 2 → 3 → 4 → 5
    input_list = [1, 2, 3, 4, 5]
    head = build_linked_list(input_list)

    # 執行反轉
    solution = Solution()
    reversed_head = solution.reverseList(head)

    # 將結果轉為 list 並輸出
    output_list = linked_list_to_list(reversed_head)
    print("反轉後的 Linked List：", output_list)
