class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True
        cur = self.head
        for _ in range(index - 1):
            if not cur.next:
                return False
            cur = cur.next
        if not cur.next:
            return False
        if cur.next == self.tail:
            self.tail = cur
        cur.next = cur.next.next
        return True

    def getValues(self) -> List[int]:
        res = []
        cur = self.head
        while cur:
           res.append(cur.val)
           cur = cur.next
        return res