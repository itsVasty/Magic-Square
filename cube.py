import numpy as np

class Cube:

	def __init__(self, n, cube = np.array([])):
		self.n = n if cube.size == 0 else len(cube[0, :])
		self.cube = np.zeros((n,n)) if cube.size == 0 else cube

	def __str__(self):
		return "n = %d \n %s" % (self.n, self.cube)

	def solve(self):
		i, j = 0, (self.n-1)//2

		self.cube[i, j] = 1

		for num in range(2, self.n**2):
			k = (i-1) if i >= 1 else (n-1)
			l = (j-1) if j >= 1 else (n-1)

			if self.cube[k, l] >= 1:
				i = (i+1)%n
			else:
				i, j = k, 1

			self.cube[i, j] = num



	def validate(self):
		valid = False
		total, _total = sum(self.cube[0, :]), 0

		#print("total: %d" % (total))

		for i in range(1, self.n):
			_list = self.cube[i, :]
			valid, _total = self.__validate(_list, total)

			#print("row %d: %s, \n total: %d" % (i, _list, _total))

			if not valid:
				print("validation failed! \n Test Value: %d \n Actual Value: %d" % (total, _total))
				return False 

		for j in range(0, self.n):
			_list = self.cube[:, j]
			valid, _total = self.__validate(_list, total)

			#print("col %d: %s, \n total: %d" % (j, _list, _total))

			if not valid:
				print("validation failed! \n Test Value: %d \n Actual Value: %d" % (total, _total))
				return False 
				
		pos_diag, neg_diag = np.diag(self.cube), np.diag(self.cube[::-1])[::-1]


		valid, _total = self.__validate(pos_diag, total)
		#print("positive diagonal: %s, \n total: %s" % (pos_diag, _total))
		if not valid:
			print("validation failed! \n Test Value: %d \n Actual Value: %d" % (total, _total))
			return False 

		valid, _total = self.__validate(neg_diag, total)
		#print("negative diagonal: %s, \n total: %s" % (neg_diag, _total))
		if not valid:
			print("validation failed! \n Test Value: %d \n Actual Value: %d" % (total, _total))
			return False

		print("Valid!")
		return True



	def __validate(self, _list, total):
		_total = sum(_list)
		return total == _total, _total


a = np.array([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
cube = Cube(5)
print(cube)
cube.solve()
print(cube)


