class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

# def getNthFromLast(head,n):
#     length = 0
#     curr = head

#     if head == None or n <= 0:
#         return
    
#     while curr != None:
#         length += 1
#         curr = curr.next
        
#     if n > length:
#         return -1
        
#     curr = head
#     for i in range(1, length - n + 1):
#         curr = curr.next
        
#     return curr.data
        
def getNthFromLast(head,n):
    if head == None:
        return None
        
    slow = head
    fast = head
    
    for i in range(n):
        if fast == None:
            return -1
        
        fast = fast.next
        
    while fast != None:
        slow = slow.next
        fast = fast.next
        
    return slow.data

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# display_linked_list(head)
print(getNthFromLast(head, 2))