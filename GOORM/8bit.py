n = int(input())
li = input().split()
li = [int(x) for x in li]
dec = sum(li)

# Function to convert decimal to octal
def decimal_to_octal(num):
    if num == 0:
        return "0"
    octal_num = ""
    while num > 0:
        remainder = num % 8
        octal_num = str(remainder) + octal_num
        num = num // 8
    return octal_num

# Convert the decimal sum to octal
octal_result = decimal_to_octal(dec)

print(octal_result)
