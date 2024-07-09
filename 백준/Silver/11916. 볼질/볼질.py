class Baseball:
	def __init__(self):
		self.base1 = False
		self.base2 = False
		self.base3 = False
		self.score = 0
		self.ballcount = 0

	def oneCount(self, number):
		# 볼인 경우
		if number == 1: 
			if self.ballcount == 3:
				if not self.base1:
					self.base1 = True
					self.ballcount = 0
				elif not self.base2:
					self.base2 = True
					self.ballcount = 0
				elif not self.base3:
					self.base3 = True
					self.ballcount = 0
				else:
					self.ballcount = 0
					self.score += 1
			else:
				self.ballcount += 1

		# 몸에 맞는 공
		elif number == 2:
			if not self.base1:
				self.base1 = True
				self.ballcount = 0
			elif not self.base2:
				self.base2 = True
				self.ballcount = 0
			elif not self.base3:
				self.base3 = True
				self.ballcount = 0
			else:
				self.ballcount = 0
				self.score += 1

		# 폭투인 경우
		elif number == 3:
			if self.ballcount == 3:
				if self.base3:
					self.base3 = False
					self.score += 1
				if self.base2:
					self.base2 = False
					self.base3 = True
				if self.base1:
					self.base1 = False
					self.base2 = True
				self.ballcount = 0
				self.base1 = True
			else:
				if self.base3:
					self.base3 = False
					self.score += 1
				if self.base2:
					self.base2 = False
					self.base3 = True
				if self.base1:
					self.base1 = False
					self.base2 = True
				self.ballcount += 1

N = int(input())
numbers = list(map(int, input().split()))

baseball = Baseball()

for num in numbers:
	baseball.oneCount(num)

print(baseball.score)