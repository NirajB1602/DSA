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

# def deleteHead(head):
#     if head == None:
#         return None
        
#     elif head.next == head:
#         return None
        
#     else:
#         curr = head
#         while curr.next != head:
#             curr = curr.next
            
#         temp = head.next
#         curr.next = temp
#         head.next = None
#         return temp
        
def deleteHead(head):
    if head == None:
        return None
        
    elif head.next == head:
        return None
        
    else:
        head.data = head.next.data
        head.next = head.next.next
        return head
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

lst = deleteHead(head)
displayList(lst)