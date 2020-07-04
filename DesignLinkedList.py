class Node:
    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.prev = prev_node
        self.next = next_node
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(float("-inf"), None, None)
        self.tail = Node(float("inf"), None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.length > index:
            i = 0
            node = self.head.next
            while i!= index:
                node = node.next
                i += 1
            return node.value
        return -1
        #self._print()

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val, self.head, self.head.next)
        node.prev.next = node
        node.next.prev = node
        self.length += 1
        #self._print()

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val, self.tail.prev, self.tail)
        node.prev.next = node
        node.next.prev = node
        self.length += 1
        #self._print()

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        i = 0
        curr_node = self.head.next
        while i!= index:
            curr_node = curr_node.next
            i += 1  
            
        node = Node(val, curr_node.prev, curr_node)
        node.prev.next = node
        node.next.prev = node
        self.length += 1
        #self._print()

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.length > index:
            i = 0
            curr_node = self.head.next
            while i!= index:
                curr_node = curr_node.next
                i += 1  

            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev
            self.length -= 1
            #self._print()
        
    def _print(self):
        output = "length:{} ".format(self.length)
        curr = self.head
        while curr:
            output += "->{}".format(curr.value)
            curr = curr.next
        print(output)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
