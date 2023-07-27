from collections import deque

def solution(phone_book):
    phone_book.sort() # ['119', '1195524421', '97674223']
    phone_book = deque(phone_book)
    hash_table = {}
    result = True
    
    for j in range(len(phone_book)):
        compare = phone_book.popleft()
        for i in phone_book:
            hash_table[i[:len(compare)]] = 1
        if compare in hash_table:
            result = False
            return result
        else:
            hash_table = {}
            
            
    
    
    return result