# (1,1)
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
      
# Hashmap
# 1, (1,1)
# 2, (2,2)
class hashmap:
    def __init__(self, capacity):
        self._map = [Node("default", "default")]*capacity
        self.capacity = capacity
        
    def _print_(self):
        items = ""
        for i in range(self.capacity):
            item = self._map[i]
            items = " i:"+str(i)+" ==> ("
            while item:
                items += str(item.key)+":"+str(item.value)+" | "
                item = item.next
            items += ") "
        print (items)
        return items
    
    def _hash(self, key):
        return key%self.capacity


    def has_key(self, key):
        index = self._hash(key)
        node = self._map[index]
        
        while node.next:
            node = node.next
            if node.key == key:
                return True

        return False
    
    def get(self, key):
        index = self._hash(key)
        node = self._map[index]
        
        while node.next:
            node = node.next
            if node.key == key:
                return node

        return -1
    
    def put(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)
        
        prev = self._map[index]
        curr = prev.next
        print("put index:"+str(index))
        # Add to linked list
        while curr:
            #print("hashmap put key:"+ str(curr.key) + " value:" + str(curr.value))
            if curr.key == key:
                curr.value = value
                #print("match found")
                return 2
            prev = curr
            curr = curr.next
        prev.next = new_node
        #print("match not found")
        return 1
    
    def del_node(self, key):
        #print("del_node:"+str(key))
        index = self._hash(key)
        prev = self._map[index]
        curr = prev.next
        #print("index:"+str(index))

        # Remove from linked list
        while curr.next:
            if curr.key == key:
                #print("Deleting key:"+ str(key))
                prev.next = curr.next
                curr.next = None
                return
            prev = curr
            curr = curr.next  
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = [-1 for _ in range(capacity)]
        self.hashmap = hashmap(capacity)
        self.capacity = capacity

    def get(self, key: int) -> int:
        node = self.hashmap.get(key)
        
        if node != -1:
            #print("get key:"+ str(node.key) + " value:" + str(node.value))
            self.cache.remove(key)
            self.cache.insert(0, key)
        #else:
            #print("get key:"+ str(key) + " value:" + str(node))
        
        #print("cache: "+ str(self.cache)+" hashmap: ")
        #self.hashmap._print_()
        if node != -1:
            return node.value
        else:
            return node

    def put(self, key: int, value: int) -> None:
        #print("put key:"+ str(key) + " value:" + str(value))
        resp = self.hashmap.put(key, value)
        try:
            self.cache.remove(key)
        except ValueError:
          print("Unable to find key "+ str(key))

        self.cache.insert(0, key)
        
        while len(self.cache) > self.capacity:
            new_capacity = len(self.cache)
            del_key = self.cache[new_capacity-1]
            self.cache.pop(new_capacity-1)
            self.hashmap.del_node(del_key)
           
        
        #print("cache: "+ str(self.cache)+" hashmap: ")
        #self.hashmap._print_()
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
