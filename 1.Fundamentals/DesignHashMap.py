class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [Node(None, None) for _ in range(10000)]

    def hashedIndex(self, key):
        return key % 9999
    
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = self.hashedIndex(key)
        curr = self.map[idx]
        updated = False
        
        while curr.next:
            curr = curr.next
            if curr.key == key:
                curr.value = value
                updated = True
                break
            
        if not updated:
            curr.next = Node(key, value)


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = self.hashedIndex(key)
        curr = self.map[idx]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = self.hashedIndex(key)
        prev = self.map[idx]
        curr = prev.next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
