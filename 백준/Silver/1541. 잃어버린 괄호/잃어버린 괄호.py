def solve(st):
    parts = st.split("-")
    total = sum(map(int, parts[0].split("+")))
    
    for part in parts[1:]:
        total -= sum(map(int, part.split("+")))
    
    return total
        
st = input()
print(solve(st))