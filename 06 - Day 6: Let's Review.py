# ===================================
#   Problem statement & information
# ===================================

# Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a 
# single line (see the Sample below for more detail). Note: 0 is considered to be an even index.

# Difficulty: Easy
# Max Score: 30
# Language: Python

# ===================================
#             Solutions
# ===================================

# ===================================
#             Method 1
# ===================================


#!/bin/python3

def string_print(input_list):
    even_list, odd_list = [], []
    for k in range(len(input_list)):
        if k % 2 == 0:
            even_list.append(input_list[k])
        else:
            odd_list.append(input_list[k])
    print(''.join(even_list) + ' ' + ''.join(odd_list))
    
    return
    
def output(number):
    for k in range(number):
        user_list = list(input().rstrip())
        string_print(user_list)
    return

    
if __name__ == '__main__':
    
    output(int(input()))


# ===================================
#             Method 2
# ===================================

#!/bin/python3

class Output:
    
    def __init__(self, number, input_list):
        self.number = case_num
        self.input_list = string
        
    def string_print(self):
        even_list, odd_list = [], []
        for k in range(len(self.input_list)):
            if k % 2 == 0:
                even_list.append(self.input_list[k])
            else:
                odd_list.append(self.input_list[k])
        print(''.join(even_list) + ' ' + ''.join(odd_list))
        
    
if __name__ == '__main__':
    
    case_num = int(input())
    
    for k in range(case_num):
        string = list(input().rstrip())
        out = Output(case_num, string)
        out.string_print()
