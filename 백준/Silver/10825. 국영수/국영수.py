def sort_students(students):
	"""
	Sorts students based on the following order:
	1) Decreasing korean score
	2) Increasing english score
	3) Decreasing math score
	4) Increasing name order. 
	(Uppercase are smaller than lowercase in ASCII so they come first alphabetically.)
	"""
	students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
	return students



n = int(input())
students = []
for i in range(n):
	name, kor, eng, math = map(str, input().split())
	students.append((name, kor, eng, math))

students = sort_students(students)

for student in students:
    print(student[0])