class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def insertInMid(head,x):
    #code here
    temp = Node(x)
    
    slow = head
    fast = head
    
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        
    temp.next = slow.next
    slow.next = temp

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

insertInMid(head, 25)

display_linked_list(head)