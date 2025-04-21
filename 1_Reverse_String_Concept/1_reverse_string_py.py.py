

'''Method1
 Reverse String through Slicing
 Slicing: Quick, clean, and readable.  '''

def reverse_string_method1(s):
    return s[::-1]                ###Output: manroS
    
 
'''Method2
 Reverse String through Looping
 Looping: Good for manual manipulation, teaches string handling.'''
def reverse_string_method1(s):
    reverse_str = ""
    for char in s:
        reverse_str = each + reverse_str

    return reverse_str          ###Output: manroS

'''Method3
 Reverse String through reversed() and join()
 reversed() + join(): Efficient and Pythonic for string reversal.'''

def reverse_string_method3(s):
    return ''.join(reversed(s))  ###Output: manroS


'''Method4
Using Recursion method
Recursion: Great for understanding recursion and solving problems recursively.'''

def reverse_string_method4(s):
    if len(s)==0:
        return s
    return reverse_string_method4(s[1:])+ s[0]  ###Output: manroS
    
'''Method5
Using Stack List 
Stack: Stack: Good for learning data structures, especially LIFO.'''   
def reverse_string_method5(s):    
    stack = list(s)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str                 ###Output: manroS 

'''Method6
Using Stack List 
List Comprehension: Compact, Pythonic solution using comprehension.

'''   
def reverse_string_method6(s):        
    return ''.join([s[i] for i in range(len(s)-1, -1, -1)]) ###Output: manroS


'''Method7
In-place Reversal (using list manipulation)
In-place Reversal: Memory-efficient for large data sets, modifies the string directly.'''
def reverse_string(s):
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)




#main
input_string = "Sornam"
reverse_string_output1 = reverse_string_method1(input_string)
reverse_string_output2 = reverse_string_method2(input_string)
reverse_string_output3 = reverse_string_method3(input_string)
reverse_string_output4 = reverse_string_method4(input_string)
reverse_string_output5 = reverse_string_method5(input_string)
reverse_string_output6 = reverse_string_method6(input_string)
reverse_string_output7 = reverse_string_method7(input_string)

print("Input String: ", input_string)

print("Reversed String through Slicing (Method1):", reverse_string_output1)
print("Reversed String through Looping (Method2): ", reverse_string_output2)
print("Reversed String through Reverse and Join (Method3):", reverse_string_output3)
print("Reversed String through Recursion (Method4):", reverse_string_method4(input_string))
print("Reversed String through Recursion (Method4):", reverse_string_method4(input_string))
print("Reversed String through Stack(Method5):", reverse_string_output5)
print("Reversed String through List Comprehension(Method6):", reverse_string_output6)
print("Reversed String through In-place Reversal(Method7):", reverse_string_output7)



