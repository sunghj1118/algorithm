k = int(input())
our_answers = input()
friend_answers = input()

n = len(our_answers) # num questions

different = sum(1 for y, f in zip(our_answers, friend_answers) if y != f)
same = n - different

# max possible score
max_score = max(min(k, n - k), min(k + different, n - k + same))

print(max_score)