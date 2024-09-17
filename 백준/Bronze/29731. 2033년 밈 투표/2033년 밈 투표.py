def astley(lyrics):
	original = [
	"Never gonna give you up",
	"Never gonna let you down",
	"Never gonna run around and desert you",
	"Never gonna make you cry",
	"Never gonna say goodbye",
	"Never gonna tell a lie and hurt you",
	"Never gonna stop"
	]

	for lyric in lyrics:
		if lyric not in original:
			return True

	return False


n = int(input())
arr = []
for _ in range(n):
	arr.append(input())

print("Yes" if astley(arr) == True else "No")