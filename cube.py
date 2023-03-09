import numpy as np

class Cube:
	# ------------------------------------------------------- #
	# Magic-Cube Constructor								  #
	# Optional value for cube for testing					  #
	# ------------------------------------------------------- #
	def __init__(self, N, cube = np.array([[]])):
		n, m = np.shape(cube)

		if not cube.size or n != m:
			self.n = N
			self.cube = np.zeros((N,N))
			self.__generate()
		else:
			self.n = n
			self.cube = cube

	# ------------------------------------------------------- #
	# Magic-Cube toString									  #
	# ------------------------------------------------------- #
	def __str__(self):
		return "cube:\n%s\n\nn = %d" % (self.cube, self.n)


	# ------------------------------------------------------- #
	# Magic-Cube Generator                                    #
	# ------------------------------------------------------- #
	def __generate(self):
		i, j = 0, (self.n-1)//2

		self.cube[i, j] = 1

		for num in range(2, (self.n**2)+1):

			k, l = (i-1)%self.n, (j+1)%self.n


			if (self.cube[k, l] >= 1) | (i == 0 & j == self.n-1):
				k, l = i+1, j

			i, j = k, l

			self.cube[i, j] = num

		# print(self.cube)


	# ------------------------------------------------------- #
	# Magic-Cube Validator                                    #
	# ------------------------------------------------------- #
	def validate(self):
		valid = False
		total, _total = sum(self.cube[0, :]), 0

		# Row Validation
		for i in range(1, self.n):
			valid, _total = self.__check(self.cube[i, :], total)

			if not valid:
				print("validation failed!\nTest Value: %d\nActual Value: %d" % (total, _total))
				return False 


		# Column Validation
		for j in range(0, self.n):
			valid, _total = self.__check(self.cube[:, j], total)

			if not valid:
				print("validation failed!\nTest Value: %d\nActual Value: %d" % (total, _total))
				return False 


		# Diagonals Extraction		
		pos_diag, neg_diag = np.diag(self.cube), np.diag(self.cube[::-1])[::-1]


		# Positive Diagonal Validation
		valid, _total = self.__check(pos_diag, total)

		if not valid:
			print("validation failed!\nTest Value: %d\nActual Value: %d" % (total, _total))
			return False 


		# Negative Diagonal Validation
		valid, _total = self.__check(neg_diag, total)

		if not valid:
			print("validation failed!\nTest Value: %d\nActual Value: %d" % (total, _total))
			return False

		# Validation Passed
		print("Cube:\n%s\nN = %d\nTotal = %d\nValid!" % (self.cube, self.n, total))
		return True


	# ------------------------------------------------------- #
	# List Validation Method                                  #
	# ------------------------------------------------------- #
	def __check(self, _list, total):
		_total = sum(_list)
		return total == _total, _total


a = np.array([
	          [8, 1, 6],
	          [3, 5, 7],
	          [4, 9, 2]
	        ])

b = np.array([
			  [17, 24, 1, 8, 15],
	          [23, 5, 7, 14, 16],
	          [4, 6, 13, 20, 22],
	          [10, 12, 19, 21, 3],
	          [11, 18, 25, 2, 9]
	         ])

c = np.array([
			  [30, 39, 48, 1, 10, 19, 28],
	          [38, 47, 7, 9, 18, 27, 29],
	          [46, 6, 8, 17, 26, 35, 37],
	          [5, 14, 16, 25, 34, 36, 45],
	          [13, 15, 24, 33, 42, 44, 4],
	          [21, 23, 32, 41, 43, 3, 12],
	          [22, 31, 40, 49, 2, 11, 20]
	         ])

cube = Cube(11)
cube.validate()


