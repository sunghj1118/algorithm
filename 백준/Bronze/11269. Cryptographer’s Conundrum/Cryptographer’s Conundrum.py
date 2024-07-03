s = input()

def check_str(s):
    if len(s) % 3 != 0:
        return -1
    
    count = 0
    for i in range(0, len(s), 3):
        if s[i].lower() != 'p':
            count += 1
        
        if s[i+1].lower() != 'e':
            count += 1
            
        if s[i+2].lower() != 'r':
            count += 1
    
    return count

print(check_str(s))