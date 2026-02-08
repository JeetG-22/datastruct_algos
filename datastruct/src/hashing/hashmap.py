class Node: 
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = [None] * capacity
        self.size = 0


    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        node = self.hash[index]

        if not node:
            self.hash[index] = Node(key, val)
        else:
            while node.next:
                if node.key == key:
                    node.val = val
                    return
                node = node.next
            node.next = Node(key, val)
        self.size += 1
        if self.size / self.capacity >= .5:
            self.resize()

    
    def hash_function(self, key):
        return key % self.capacity
        


    def get(self, key: int) -> int:
        return



    def remove(self, key: int) -> bool:
        return


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        self.capacity *= 2
        self.size = 0

        old_hash = self.hash
        self.hash = [None] * self.capacity


        for node in old_hash:
            while node:
                self.insert(node.key, node.val)
            
            



