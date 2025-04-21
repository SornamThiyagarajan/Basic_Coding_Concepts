'''Method1
 Reverse String through Looping'''


def reverse_string_method1(s):
    reverse_str = ""
    for each in s:
        reverse_str = each + reverse_str

    return reverse_str

'''Method2
 Reverse String through Slicing'''

def reverse_string_method2(s):
    return s[::-1]


'''Method3
 Reverse String through reversed() and join()'''

def reverse_string_method3(s):
    return ''.join(reversed(s))


'''Method4
Using Recursion method'''

def reverse_string_method4(s):
    if len(s)==0:
        return s
    return reverse_string_method4(s[1:])+ s[0]

#main
input_string = "Sornam"
reverse_string_output1 = reverse_string_method1(input_string)
reverse_string_output2 = reverse_string_method2(input_string)
reverse_string_output3 = reverse_string_method3(input_string)
reverse_string_output4 = reverse_string_method4(input_string)

print("Input String: ", input_string)
print("Reversed String through Looping (Method1): ", reverse_string_output1)
print("Reversed String through Slicing (Method2):", reverse_string_output2)
print("Reversed String through Reverse and Join (Method3):", reverse_string_output3)
print("Reversed String through Recursion (Method4):", reverse_string_method4(input_string))



'''

'''
