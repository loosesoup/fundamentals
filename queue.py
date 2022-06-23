from linkedlist_playground import LinkedList

class queue:

	def __init__(self):
		self.queue = LinkedList()
		self.size = 0

	def enqueue(self,val):
		self.queue.insert_at_end(val)
		self.size +=1

	def dequeue(self):
		try:
			self.size -=1
			val = self.queue.head.data
			self.queue.remove_at(0)
			return val
		except AttributeError as e:
			print('queue is empty')

	def peek(self):
		if self.size < 1:
			raise Exception('queue is empty') 
		return self.queue.head.data

	def isEmpty(self):
		return self.size == 0

	def len(self):
		return self.size

if __name__ == '__main__':
	pass