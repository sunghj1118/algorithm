def min_operations_to_transform(n, B):
    operations = 0

    while any(B):
        for i in range(n):
            if B[i] % 2 == 1:
                B[i] -= 1
                operations += 1

        if any(B):
            for i in range(n):
                B[i] //= 2
            operations += 1

    return operations

n = int(input())
items = list(map(int, input().split()))

# need to find if its better to 
# A) add1 to a single value or 1
# B) multiplyx2 to all values
# such that our array of [0]*n == items

# Work backwards
# If even, divide by two.
# If odd, add by 1.

print(min_operations_to_transform(n, items))