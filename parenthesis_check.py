class parenthesis_checking():
	def __init__(self):
		self.stack = []

	def check(self, exp):
		for i in range(len(exp)):
			if exp[i]=='(' or exp[i] == '{' or exp[i] == '[':
				self.stack.append(exp[i])
				continue

			if len(self.stack) == 0:
				return 0	

			if exp[i] == ')':
				char = self.stack.pop()
				if char != '(':
					return 0		
			if exp[i] == '}':
				char = self.stack.pop()
				if char != '{':
					return 0		
			if exp[i] == ']':
				char = self.stack.pop()
				if char != '[':
					return 0	
		if len(self.stack):
			return 0
		else:
		    return 1

par = parenthesis_checking()

exp = "[(){}([{}])]"	

print(par.check(exp))

