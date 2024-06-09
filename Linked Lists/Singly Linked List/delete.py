class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next
    print()

# 1st approach 
def delete_head(head):
    if head == None:
        return
    
    if head.next == None:
        return None
    
    temp = head.next
    head.data = temp.data
    head.next = temp.next
    return head

# 2nd approach 
def delete_Head(head):
    if head == None:
        return
    
    if head.next == None:
        return None
        
    temp = head.next
    head.next = None
    return temp

def delete_Tail(head):
    if head == None or head.next == None:
        return None
    
    curr = head
    while curr.next.next != None:
        curr = curr.next
        
    curr.next = None
    return head

def delete_At_Position(head, pos):
    curr = head
    
    if pos == 1:
        temp = head.next
        return temp
        
    for i in range(pos - 2):
        curr = curr.next
        if curr == None:
            return head
            
    # if curr.next.next == None:
    #     curr.next = None
    #     return head
        
    curr.next = curr.next.next
    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# display_linked_list(head)

# lst1 = delete_Head(head)
# display_linked_list(lst1)

# lst2 = delete_Tail(head)
# display_linked_list(lst2)

lst3 = delete_At_Position(head, 2)
display_linked_list(lst3)