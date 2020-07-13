class A():
	def say(self):
		print('A:',self)
class B(A):
	def say(self):
		A().say()
		print('B:',self)

B().say()

class Aa():
	def say(self):
		print('Aa:',self)
class Bb(Aa):
	def say(self):
		super().say() #和上面的 A()一样都是调用父类方法
		print('Bb:',self)

Bb().say()