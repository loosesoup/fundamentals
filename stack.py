class Stack :
	"""implementing ADS Stack"""
	def __init__(self):
		self.stack = []
		self.len = 0

	def pop(self):
		# pop from end of stack and return it
		try:
			self.len -=1
			return self.stack.pop() 
		except IndexError:
			print("cannot remove from empty stack")

	def push(self,val):
		# push element to end of stack
		self.stack.append(val)
		self.len +=1

	def empty(self):
		# is stack empty?
		return not self.stack

	def top(self):
		# return the element on top of the stack
		if self.stack: return self.stack[-1]
		raise Exception("stack has no elements")

	def size(self):
		# returns the len of stack
		return len(self.stack)

if __name__ == '__main__':
	pass
