# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        carry = 0

        while l1 and l2:
            total = l1.val + l2.val + carry
            digit = total % 10
            carry = total // 10
            node = ListNode(digit)
            tail.next = node
            tail = tail.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val + carry
            digit = total % 10
            carry = total // 10
            tail.next = ListNode(digit)
            tail = tail.next

            l1 = l1.next

        while l2:
            total = l2.val + carry
            digit = total % 10
            carry = total // 10
            tail.next = ListNode(digit)
            tail = tail.next

            l2 = l2.next

        if carry:
            tail.next = ListNode(1)

        return head.next
