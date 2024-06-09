# def ispar(s):
#     stack = [] 

#     for char in s:
#         if char in ['{','[','('] : 
#             stack.append(char) 
        
#         else:       
            
#             if len(stack) == 0: 
#                 return False
            
#             elif char == '}' and stack[-1] == '{':
#                     stack.pop()
                    
#             elif char == ')' and stack[-1] == '(':
#                     stack.pop()
                    
#             elif char == ']' and stack[-1] == '[':
#                     stack.pop()
                    
#             else:
#                 return False  
    
#     if stack: 
#         return False
        
#     return True

# s = "(){}[])"
# print(ispar(s))

open_list = ["[","{","("]
close_list = ["]","}",")"]

# Function to check parentheses
def check(myStr):
	stack = []
	for i in myStr:
		if i in open_list:
			stack.append(i)
		elif i in close_list:
			pos = close_list.index(i)
			if ((len(stack) > 0) and
				(open_list[pos] == stack[len(stack)-1])):
				stack.pop()
			else:
				return "Unbalanced"
	if len(stack) == 0:
		return "Balanced"
	else:
		return "Unbalanced"


# Driver code
string = "{[]{()}}"
print(string,"-", check(string))

string = "[{}{})(]"
print(string,"-", check(string))

string = "((()"
print(string,"-",check(string))