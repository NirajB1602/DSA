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

# def insertInHead(head,x):
#     temp = Node(x)
#     if head == None:
#         temp.next = temp
#         return temp
        
#     else:
#         curr = head
#         while curr.next != head:
#             curr = curr.next
        
#         temp.next = head
#         curr.next = temp
#         return temp
    
def insertInHead(head,x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
        
    else:
        temp.next = head.next
        head.next = temp
        head.data, temp.data = temp.data, head.data
        return head
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

lst = insertInHead(head, 100)
displayList(lst)