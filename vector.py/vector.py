class Vector:
	i = int() 
	j = int() 
	k = int()

	def __init__(self, i, j, k):
		self.i = i
		self.j = j
		self.k = k  

	def dotProd(self, vector):
		return (self.i * vector.i) + (self.j * vector.j) + (self.k * vector.k)

	def dotAngle(self, vector):
		import math
		length1 = math.sqrt(self.i**2.0 + self.j**2.0 + self.k**2.0)
		length2 = math.sqrt(vector.i**2.0 + vector.j**2.0 + vector.k**2.0)
		angle = math.acos((self.dotProd(vector))/(length1*length2))
		return angle

	def dotPerp(self, vector):
		if self.dotAngle(vector) < 0: 
			return " The angle between the vectors is acute. "
		elif self.dotAngle(vector) == 0: 
			return " The vectors are perpendicular. "
		else:
			return " The angle between the vectors is obtuse. "

	def crosProd(self, vector):
		return ((self.k * vector.j) + (self.j * vector.k)) - ((self.k * vector.i ) + (self.i * vector.k)) + ((self.j * vector.i ) + (self.i * vector.j))

	def ariaXProd(self, vector):
		return abs(((self.k * vector.j ) + (self.j * vector.k)) - ((self.k * vector.i ) + (self.i * vector.k)) + ((self.j * vector.i ) + (self.i * vector.j)))

vector1 = Vector(-5, 1, 2)
vector2 = Vector(3, 6, 2)
print(vector1.dotProd(vector2))
print(vector1.dotAngle(vector2))
print(vector1.dotPerp(vector2))
print(vector1.crosProd(vector2))
print(vector1.ariaXProd(vector2))