class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    # 同时pop之前判断队列当前是否为空。
    def pop(self, value):
        if self.items and value == self.items[0]:
            self.items.pop(0)

    # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    # 这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        print(self.items)
        while self.items and value > self.items[-1]:
            self.items.pop()
        self.items.append(value)

    def front(self):
        return self.items[0]


# input code
Ncount = int(input())
Nin = input()
Nlist = [int(j) for j in Nin.split()]

# enumerate
a = [1, 2, 3, 4, 5]
a = enumerate(a)
for index, value in a:
    print(index, value)

# double list sort
a = [[6, 1], [2, 6], [4, 5]]
a = sorted(a, key=lambda x: x[0])
