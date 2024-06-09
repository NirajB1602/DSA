class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def displayList(head):
    if head == None:
        return None
        
    print(head.data)
    curr = head.next
    while curr != head:
        print(curr.data)
        curr = curr.next

def insertAtPosition(head,pos,data):
    temp = Node(data)
    if pos == 1:
        temp.next = head.next
        head.next = temp
        return head
        
    else:
        curr = head
        for i in range(pos - 1):
            if curr.next == head:
                return head
            curr = curr.next
            
        temp.next = curr.next
        curr.next = temp
        return head
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

lst = insertAtPosition(head,2, 100)
displayList(lst)