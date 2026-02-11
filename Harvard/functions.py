# lst = [3, 8, 2, 0, 5, -1, 6, 4, 2, 7, 9]

# def second_largest(lst):
#     largest = float('-inf')
#     second_largest = float('-inf')

#     for num in lst:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif  second_largest < num < largest:
#             second_largest = num
#     if second_largest == float('inf'):
#         return None
#     return second_largest

# print(second_largest(lst))

# def fibonacci(n):
#     a, b = 0, 1
#     k = 1
#     print(b)
#     while k <= n:
#         p = a + b
#         print(p)
#         a , b = b, p
#         k += 1
        
# fibonacci(7)

states_to_capitals = {
    'Texas': "Austin",
    'New York': 'Albany'
}

# print(states_to_capitals['New York'])
primary_colors = {'red', 'blue', 'yellow'}
# color = 'green'
# print(primary_colors.issuperset({'red'}))
# print(primary_colors.add('tomato'))
# from collections import deque

# mylist = []
# myqueue = deque()
# myqueue.append('1')
# k = 1
# while k <= 6:
#     a = myqueue.popleft()
#     mylist.append(int(a))
#     myqueue.append(str(a) + '0')
#     myqueue.append(str(a) + '1')
#     k += 1

# print(mylist)
# print(int('101', 2))


# from collections import deque

# def generate_binary(n):
#     if n <= 0:
#         return []
        
#     mylist = []
#     myqueue = deque(['1']) # Initialize with the first binary number
    
    
#     for _ in range(n):
#         # 1. Get the next binary string from the front
#         current = myqueue.popleft()
        
#         # 2. Add it to our results (converting to int as per your original code)
#         mylist.append(int(current))
        
#         # 3. Generate the next two numbers by appending 0 and 1
#         myqueue.append(current + '0')
#         myqueue.append(current + '1')
        
#         print(myqueue)

#     return mylist

# print(generate_binary(7))
# Example usage:
# print(generate_binary(5)) 
# Output: [1, 10, 11, 100, 101]
# from collections import deque


s = '{}(([]()))(({}))'
def is_valid(s):
    mappings = {'}': '{', ')': '(', ']': '['}
    
    stack = []
    
    for char in s:
        if char in mappings:
            top_element = stack.pop() if stack else '#'
            print('After popping', stack)
            
            if mappings[char] != top_element:
                return False
        else:
            stack.append(char)
            print("After Appending", stack)
            
    return not stack

print(is_valid(s))
        