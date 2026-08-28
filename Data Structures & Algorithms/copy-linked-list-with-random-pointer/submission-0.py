"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_new={}
        curr=head
        while curr:
            old_new[curr]=Node(curr.val)
            curr=curr.next

        curr=head
        while curr:
            old_new[curr].next=old_new.get(curr.next)
            old_new[curr].random=old_new.get(curr.random)
            curr=curr.next
        return old_new.get(head)
        


