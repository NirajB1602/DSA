class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def displayList(head):
    if head == None:
        return None
        
    print(head.data)
    
    curr = head.next
    while curr != head:
        print(curr.data)
        curr = curr.next
        
def insertInhead(head,data):
    temp = Node(data)
    
    if head == None:
        return temp
        
    temp.next = head
    head.prev = temp
    return temp

def findMiddle(head):
    if head == None:
        return None
            
    slow = head
    fast = head
        
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next
            
    return slow.data

head = Node(10)
temp = insertInhead(head, 20)
temp = insertInhead(temp, 30)
head.next = temp

# displayList(temp)
print(findMiddle(head))



