# 237. Delete Node in a Linked List

## Problem Statement

Given a linked list node, implement a method `deleteNode` to delete the node in-place without returning anything. The provided node is guaranteed to be a valid node from the linked list.

## Example

```python
# Input
node = 5 -> 3 -> 8 -> 2

# Usage
solution = Solution()
solution.deleteNode(node.next)  # Deletes the node with value 3

# Output
node = 5 -> 8 -> 2
```

## Solution

To delete a node from a linked list in-place, we can update the value of the given node to be the value of its next node, and then update the next pointer of the given node to skip the next node. This effectively removes the given node from the linked list.

Here is the implementation in Python:

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```

## Usage

1. Create a linked list or obtain a reference to a valid node in an existing linked list.
2. Instantiate the `Solution` class.
3. Call the `deleteNode` method on the solution object, passing the node to be deleted as the argument.

```python
# Example Usage
node = ListNode(5)
node.next = ListNode(3)
node.next.next = ListNode(8)
node.next.next.next = ListNode(2)

solution = Solution()
solution.deleteNode(node.next)  # Deletes the node with value 3

# The linked list after deletion
# node = 5 -> 8 -> 2
```

Note: This solution modifies the given node in-place and does not return anything. Ensure that the provided node is not the last node in the linked list to avoid unexpected behavior.