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

def reverseDLL(head):
    if head == None:
        return None
            
    if head.next == None:
        return head
            
    while head != None:
        temp = head
            
        head.next, head.prev = head.prev, head.next
        head = head.prev
            
    return temp

head = Node(10)
head = insertInhead(head, 20)
head = insertInhead(head, 30)

displayList(head)
lst = reverseDLL(head)
print()
displayList(lst)