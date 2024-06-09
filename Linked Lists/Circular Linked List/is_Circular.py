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

# def isCircular(head):
#     if head.next == head:
#         return True
      
#     curr = head  
#     while True:
#         if curr.next == None:
#             return False
            
#         if curr.next == head:
#             return True
            
#         curr = curr.next

def isCircular(head):
    if head.next == head:
        return True
      
    curr = head  
    while curr.next != None:
        if curr.next == head:
            return True
            
        curr = curr.next
        
    return False

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

print(isCircular(head))
        