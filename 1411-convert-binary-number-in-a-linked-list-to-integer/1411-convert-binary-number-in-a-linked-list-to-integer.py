# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = ""
        curr = head
        while curr.next:
            num += str(curr.val)
            curr = curr.next
        num += str(curr.val)

        print(num)
        return int(num, 2)
        