class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class MyDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def size(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def insertRear(self, data):
        temp = Node(data)
        if self.rear == None:
            self.front = temp

        else:
            self.rear.next = temp
            temp.prev = self.rear

        self.rear = temp
        self._size += 1

    def insertFront(self, data):
        temp = Node(data)
        if self.front == None:
            self.rear = temp

        else:
            temp.next = self.front
            self.front.prev = temp

        self.front = temp
        self._size += 1

    def deleteFront(self):
        if self.front == None:
            return
        
        else:
            self.front = self.front.next
            if self.front == None:
                self.rear = None

            else:
                self.front.prev = None
        
        self._size -= 1

    def deleteRear(self):
        if self.rear == None:
            return 
        
        else:
            temp = self.rear.prev
            temp.next = None
            self.rear = temp

        self._size -= 1

    def getRear(self):
        if self.rear:
            return self.rear.data

    def getFront(self):
        if self.front:
            return self.front.data
        

dq = MyDeque()

print(dq.isEmpty())
dq.insertRear(10)
print(dq.getFront(),dq.getRear())
dq.insertRear(20)
print(dq.getFront(),dq.getRear())
dq.insertRear(30)
print(dq.getFront(), dq.getRear())
dq.deleteFront()
print(dq.getFront(), dq.getRear())
dq.insertFront(100)
print(dq.getFront(), dq.getRear())
dq.deleteFront()
print(dq.getFront(), dq.getRear())
