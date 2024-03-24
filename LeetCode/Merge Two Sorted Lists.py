# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        while list1 and list2:
            if list1.val > list2.val:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            elif list1.val < list2.val:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tail.next = ListNode(list1.val)
                tail.next.next = ListNode(list2.val)
                list1 = list1.next
                list2 = list2.next
                tail = tail.next

            tail = tail.next

        tail.next = list1 if list1 else list2

        return head.next