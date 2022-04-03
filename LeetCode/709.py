class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self._head = ListNode(0)
        self._count = 0


    def get(self, index: int) -> int:
        if 0<= index < self._count:
            node = self._head
            for _ in range(index+1):
                node = node.next
            return node.val
        else:
            return -1


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        elif index > self._count:
            return

        # 计数累加
        self._count += 1

        add_node = ListNode(val)
        prev_node, current_node = None, self._head
        for _ in range(index + 1):
            prev_node, current_node = current_node, current_node.next
        else:
            prev_node.next, add_node.next = add_node, current_node

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._count:
            self._count -= 1
            prev_node, current_node = None, self._head
            for _ in range(index + 1):
                prev_node, current_node = current_node, current_node.next
            else:
                prev_node.next, current_node.next = current_node.next, None



# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
print(param_1 = obj.get(0))
print(obj.addAtHead(1,2))
print(obj.addAtTail(1))
print(obj.addAtIndex(1))
print(obj.deleteAtIndex(1))