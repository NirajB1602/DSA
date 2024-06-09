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
    while curr != None:
        print(curr.data)
        curr = curr.next
        
def insertInhead(head,data):
    temp = Node(data)
    
    if head == None:
        return temp
        
    temp.next = head
    head.prev = temp
    return temp

def sortedInsert(head, x):
    temp = Node(x)
    
    if head == None:
        return temp
        
    if head.data >= temp.data:
        temp.next = head
        head.prev = temp
        return temp
      
    curr = head  
    while curr != None:
        if curr.next == None and curr.data < temp.data:
            curr.next = temp
            temp.prev = curr
            break
            
        elif curr.data >= temp.data:
            prev = curr.prev
            temp.next = curr
            curr.prev = temp
            prev.next = temp
            temp.prev = prev
            break
        
        curr = curr.next
        
    return head

head = Node(30)
head = insertInhead(head, 20)
head = insertInhead(head, 10)

displayList(head)
lst = sortedInsert(head, 40)
print()
displayList(head)