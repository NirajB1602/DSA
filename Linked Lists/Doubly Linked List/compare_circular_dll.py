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

def compareCLL(head1, head2):
    if head1 == None and head2 == None:
        return True
            
    if head1.data != head2.data:
        return False
            
    curr1 = head1.next
    curr2 = head2.next
        
    while True:
        if curr1.data != curr2.data:
            return False
                
        elif curr1.next == head1 and curr2.next == head2:
            return True
              
        elif curr1.next == head1 or curr2.next == head2:
            return False
                
        curr1 = curr1.next
        curr2 = curr2.next

head1 = Node(10)
temp1 = insertInhead(head1, 20)
temp1 = insertInhead(temp1, 30)
head1.next = temp1

head2 = Node(40)
temp2 = insertInhead(head2, 20)
temp2 = insertInhead(temp2, 30)
head2.next = temp2

# displayList(temp)
print(compareCLL(head1, head2))
