class Heap:
    """
    1) Structure Property
        -it is a complete binary tree: every level other than the last level should be filled
        -we add values left to right
    2) Order Property
        -every child (left and right subtree) must be greater than their parent
        -in heaps you can have duplicates
    
    Implementation
        -build using arrays/lists
        -starts at index 1 not 0
        -parent: i // 2
        -left child: i * 2 
        -right child: i * 2 + 1
    """
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        
        while i > 1 and self.heap[i // 2] > self.heap[i]:
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        min_val = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while i * 2 < len(self.heap):
            if i * 2 + 1 < len(self.heap) and self.heap[i*2 + 1] < self.heap[i*2] < self.heap[i]:
                self.heap[i*2+1], self.heap[i] = self.heap[i], self.heap[i*2+1]
                i = i * 2 + 1
            elif self.heap[i] > self.heap[i * 2]:
                self.heap[i*2], self.heap[i] = self.heap[i], self.heap[i*2]
                i = i * 2
            else:
                break
        return min_val
                
            

        
        
        


