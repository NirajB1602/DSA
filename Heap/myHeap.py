import math

class myHeap:
    def __init__(self):
        self.arr = []

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2
    
    def insert(self, x):
        arr = self.arr
        arr.append(x)

        i = len(arr) - 1

        while i > 0 and arr[self.parent(i)] > arr[i]:
            arr[i], arr[self.parent(i)] = arr[self.parent(i)], arr[i]
            i = self.parent(i)

    def minHeapify(self, i):
        arr = self.arr
        left_child = self.leftChild(i)
        right_child = self.rightChild(i)
        smallest = i

        n = len(arr)

        if left_child < n and arr[smallest] > arr[left_child]:
            smallest = left_child

        if right_child < n and arr[smallest] > arr[right_child]:
            smallest = right_child

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.minHeapify(smallest)

    def extractMin(self):
        arr = self.arr
        if not arr:
            return math.inf
        
        n = len(arr)
        arr[0], arr[n - 1] = arr[n - 1], arr[0]
        res = arr.pop()

        self.minHeapify(0)
        return res

    def decreaseKey(self, i, x):
        arr = self.arr
        if not arr:
            return math.inf
        
        arr[i] = x

        while i != 0 and arr[self.parent(i)] > arr[i]:
            arr[i], arr[self.parent(i)] = arr[self.parent(i)], arr[i]
            i = self.parent(i)

    def delete(self, i):
        if i < len(self.arr):
            self.decreaseKey(i, -math.inf)
            self.extractMin()


heap = myHeap()
heap.insert(5)
heap.insert(3)
heap.insert(1)
print("Min element after insertion:", heap.extractMin()) 

heap.insert(2)
heap.insert(4)
print("Heap elements:", heap.arr) 