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

def isCircular(head):
    if head == None:
        return 0
            
    curr = head
    while curr.next != None:
        if curr.next == head:
            return 1
                
        curr = curr.next
            
    return 0

# head = Node(10)
# head = insertInhead(head, 20)
# head = insertInhead(head, 30)

head = Node(10)
temp = insertInhead(head, 20)
temp = insertInhead(temp, 30)
head.next = temp

# displayList(temp)
print(isCircular(head))

