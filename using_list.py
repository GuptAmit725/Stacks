class Stacks():
	def __ini__(self):
		self.stack = []

	def isEmpty(self):
		"""
		This function checks if the stack is empty or not.
		"""
		return self.stack is None		

	def push(self,ele):
		"""
		Adds the element to the end of the stack.
		"""
		self.stack.push(ele)

	def pop(self):
		"""
		returns the last element of the stack and deletes the element permanently.
		"""
		if not self.isEmpty():
			return self.stack.pop()
		else:
			return -1

	def peek(self):
		""" 
		this function returns the last,
		element withous deleting the elemnet. 

		"""
		if not self.isEmpty():
			return self.stack[-1]
		else:
			return -1
						
s = Stacks()
print('peek')
print('pop')
print('push')
do = input('What exactly you wan to do?')

if do=='push':
	ele = input(int('inter the element you want to add. : '))
	s.push(ele)
elif do == 'pop':
	s.pop()
elif do == 'peek':
	s.peek()
else:
	print('Enter the valid operation you want tio do.')			
