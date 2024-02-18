# Add Two Numbers

## Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Solution

```python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        values = []
        for l in [l1, l2]:
            temp = l
            l_values = ''
            while True:
                l_values += str(temp.val)
                temp = temp.next
                if not temp:
                    break
            values.append(int(l_values[::-1]))

        lst = list(str(sum(values))[::-1])
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
```

This solution first iterates through both linked lists to extract the values, reverses them, sums them, and then creates a new linked list to store the result.