class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# ---- Helper functions ----
def build_linked_list(nums):
    """Convert a list like [2,4,3] into a linked list"""
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def print_linked_list(node):
    """Print linked list as 1->2->3"""
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print("->".join(values))


# ---- Main ----
if __name__ == "__main__":
    sol = Solution()

    # Example 1: 342 + 465 = 807
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)
    print_linked_list(result)  # 7->0->8

    # Example 2: 0 + 0 = 0
    l1 = build_linked_list([0])
    l2 = build_linked_list([0])
    result = sol.addTwoNumbers(l1, l2)
    print_linked_list(result)  # 0

    # Example 3: 9999999 + 9999 = 10009998
    l1 = build_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = build_linked_list([9, 9, 9, 9])
    result = sol.addTwoNumbers(l1, l2)
    print_linked_list(result)  # 8->9->9->9->0->0->0->1