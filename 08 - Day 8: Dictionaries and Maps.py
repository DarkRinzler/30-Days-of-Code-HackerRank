# ===================================
#   Problem statement & information
# ===================================

# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an 
# unknown number of names to query your phone book for. For each 'name' queried, print the associated entry from your phone book on a new line in 
# the form 'name=phoneNumber'; if an entry for 'name' is not found, print 'Not found' instead.

# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

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

def input_dict(number):
    phone_book = {}
    for k in range(number):
        entry = list(map(str, input().rstrip().split()))
        phone_book[entry[0]] = entry[1]
    while True:
        try:
            name = str(input().rstrip())
            if name in phone_book:
                print(name + '=' + str(phone_book[name]))
            else:
                print('Not found')
        except EOFError:
            break
    return
    

if __name__ == '__main__':
    
    entries = int(input().strip())
    
    input_dict(entries)
    

# ===================================
#             Method 2
# ===================================

#!/bin/python3

class Check_phone_book:
    
    def __init__(self, number):
        self.number = entries
        
    def input_check(self):
        phone_book = {}
        for k in range(self.number):
            entry = list(map(str, input().rstrip().split()))
            phone_book[entry[0]] = entry[1]
        while True:
            try:
                name = str(input().rstrip())
                if name in phone_book:
                    print(name + '=' + str(phone_book[name]))
                else:
                    print('Not found')
            except EOFError:
                break
        return
    
if __name__ == '__main__':
    
    entries = int(input().strip())
    
    c = Check_phone_book(entries)
    
    c.input_check()
    
    






