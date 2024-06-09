class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

# def isSorted(head): 
#     if head == None:
#         return 1
     
#     def increasing_sort(head):
#         curr = head
#         while True:
#             if curr.next == None:
#                 break
                
#             if curr.data > curr.next.data:
#                 return 0
            
#             curr = curr.next
                    
#         return 1   

#     def decreasing_sort(head):
#         curr = head
#         while True:
#             if curr.next == None:
#                 break
                
#             if curr.data < curr.next.data:
#                 return 0
            
#             curr = curr.next
                
#         return 1
    
#     ans1 = increasing_sort(head)
#     ans2 = decreasing_sort(head)
#     return ans1 or ans2
        
# def isSorted(head):
#     if head == None:
#         return 1
    
#     cur = head
    
#     total_length = 0
#     asc_length = 0
#     desc_length = 0
    
#     while cur.next != None:
#         if cur.data <= cur.next.data:
#             asc_length += 1
            
#         if cur.data >= cur.next.data:
#             desc_length += 1
            
#         total_length += 1
#         cur = cur.next
    
#     return int((asc_length == total_length) or (desc_length == total_length))

def isSorted(head):
    if head == None: 
        return 1
    
    slow = head
    fast = head.next
    
    counter = 0
    
    while fast.next != None:
        diff = slow.data - fast.data

        if abs(counter + diff) < abs(counter): 
            return 0
        
        counter = diff
        
        slow = slow.next
        fast = fast.next
        
    return 1

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(10)

# display_linked_list(head)
print(isSorted(head))