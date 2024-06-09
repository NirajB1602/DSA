from collections import deque

d = deque([1, 5, 2, 5, 8, 40, 5, 9, 15])

# append():- This function is used to insert the value in its argument to the right end of the deque.
d.append(100)
print("After append operation:", d)

# appendleft():- This function is used to insert the value in its argument to the left end of the deque.
d.appendleft(5)
print("After append-left operation:", d)

# pop():- This function is used to delete an argument from the right end of the deque.
d.pop()
print("After pop operation:", d)

# popleft():- This function is used to delete an argument from the left end of the deque.
d.popleft()
print("After pop-left operation:", d)

# index(ele, beg, end):- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
print("The index is:", d.index(5, 1, 5))

# insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
d.insert(4, 225)
print("After insert operation:", d)

# remove():- This function removes the first occurrence of the value mentioned in arguments.
d.remove(5)
print("After remove operation:", d)

# count():- This function counts the number of occurrences of value mentioned in arguments.
print(d.count(5))

# len(dequeue):- Return the current size of the dequeue.
print("The length of deque is:", len(d))

# Deque[0] :- We can access the front element of the deque using indexing with de[0].
print(d[0])

# Deque[-1] :- We can access the back element of the deque using indexing with de[-1].
print(d[-1])

# extend(iterable):- This function is used to add multiple values at the right end of the deque. The argument passed is iterable.
d.extend([20, 200])
print("After extend operation:", d)

# extendleft(iterable):- This function is used to add multiple values at the left end of the deque. 
# The argument passed is iterable. Order is reversed as a result of left appends.
d.extendleft([100, 10])
print("After extend-left operation:", d)

# reverse():- This function is used to reverse the order of deque elements.
d.reverse()
print("After reverse operation:", d)

# rotate():- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to the left. Else rotation is to right.
d.rotate(-2)
print("After rotate operation:", d)

