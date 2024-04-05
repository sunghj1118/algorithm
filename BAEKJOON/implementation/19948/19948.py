# Url: https://www.acmicpc.net/problem/19948

# make an array of the poem
poem = input().split()

# get the durability of the space key
n = int(input())

# get the remaining durability of each letter in the keyboard in a dictionary
durability = list(map(int, input().split()))

# Calculate whether the poem can be typed with spaces
if n < len(poem):
    print(-1)

last_letter = ''
for word in poem:
    for letter in word:
        # skip if the letter is the same as the last letter
        if letter == last_letter:
            continue
        last_letter = letter # update the last letter

        # if the letter is uppercase, convert it to lowercase
        if letter.isupper():
            letter = letter.lower()
        
        # decrease the durability of the letter
        durability[ord(letter) - ord('a')] -= 1

        # if the durability of the letter is less than 0, print -1 and break
        if durability[ord(letter) - ord('a')] < 0:
            print(-1)
            break

# Print the first letter of each word in the poem
for word in poem:
    print(word[0].upper(), end='')