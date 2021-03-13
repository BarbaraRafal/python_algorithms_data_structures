"""Given the head of a singly linked list, reverse the list, and return the reversed list."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, data: int = 0, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def val(self):
        return self.val

    @property
    def next_node(self):
        return self.next_node

    @next_node.setter
    def next_node(self, new_value):
        self._next_node = new_value

    def __repr__(self):
        return f"Node {self.val}"


class LinkedList:
    # function initialize head
    def __init__(self):
        self.head = None

    # function to reverse the linked list
    def reverse_list(self, head: ListNode) -> ListNode:
        pass


if __name__ == "__main__":
    pass
