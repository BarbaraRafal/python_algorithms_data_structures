from typing import List


class ListNode:
    def __init__(self, key: int, next_node: "ListNode" = None):
        self._key = key
        self._next_node = next_node

    @property
    def key(self) -> int:
        return self._key

    @property
    def next_node(self) -> "ListNode":
        return self._next_node

    @next_node.setter
    def next_node(self, new_node) -> None:
        self._next_node = new_node

    def __repr__(self) -> str:
        return f"Node({self.key})"


class LinkedList:
    def __init__(self):
        self._head = None
        self._current = None

    def __iter__(self) -> "LinkedList":
        self._current = self._head
        return self

    def __next__(self) -> "ListNode":
        if self._current is None:
            raise StopIteration
        node = self._current
        self._current = self._current.next_node
        return node

    # yield self._current
    # self._current = self._current.next_node

    @property
    def head(self):
        return self._head

    def prepend(self, key: int) -> None:
        new_node = ListNode(key=key, )
        # self._head = ListNode(key=key, next_node=self._head)

    def append(self, key: int) -> None:
        if self.head is None:
            self.prepend(key)
            return
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = ListNode(key=key)

    def find(self, key: int) -> "ListNode":
        current = self.head
        while current is not None and current.key != key:
            current = current.next_node
        return current

    def remove(self, key: int) -> None:
        current, prev = self.head, None

        while current is not None and current.key != key:
            prev = current
            current = current.next_node

        if prev is None:
            self._head = self._head.next_node
        elif current is not None:
            prev.next_node = current.next_node

    def get_nodes(self) -> List[ListNode]:
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(current)
            current = current.next_node
        return nodes

    #  (1)->(2)->(3)->(4)
    #   p    c    n bedziemy sie krecic w petli poki current nie wyjdzie poza liste
    #  (1)<-(2)<-(3)<-(4)
    def reverse_list(self):
        current = self._head
        prev_node = None
        while current:
            next_node = current.next_node  # wartosc nastepneg node'a
            current.next_node = prev_node  #
            prev_node = current
            current = next_node
        self.head = prev_node  # po skonczeniu petli prev bedzie wskazywal na ostatni element ktory po odwroceniu bedzie headem


def test_find_existing_key():
    linked_list = LinkedList()
    linked_list.append(42)

    assert linked_list.find(42) is not None


def test_find_non_existing_key():
    linked_list = LinkedList()

    assert linked_list.find(42) is None


def test_reverse_list():
    linked_list = LinkedList()
    data = [5, 4, 3, 2, 1]

    for i in range(5):
        linked_list.append(i)

    linked_list.reverse_list()
    expected = [i for i in range(5)]
    assert expected == []


if __name__ == "__main__":
    # test_find_existing_key()
    # test_find_non_existing_key()
    linked_list = LinkedList()
    # linked_list.append(5)
    # linked_list.append(4)
    # linked_list.append(3)
    # linked_list.append(2)
    # linked_list.append(1)
    # linked_list.append(0)
    linked_list.prepend(5)
    linked_list.prepend(4)
    linked_list.prepend(3)
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.prepend(0)
    print(linked_list.get_nodes())
    linked_list.remove(2)
    print(linked_list.get_nodes())
    print(linked_list.find(6))
