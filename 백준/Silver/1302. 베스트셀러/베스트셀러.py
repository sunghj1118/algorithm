n = int(input())
books = {}
for _ in range(n):
	book = input()
	books[book] = books.get(book,0) + 1

sorted_books = sorted(books, key=lambda x: (-books[x], x))
print(sorted_books[0])