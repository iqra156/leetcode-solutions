# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        current = head
        while current:
            # Shift previous bits left, then add current bit
            num = (num << 1) | current.val
            current = current.next
        return num
