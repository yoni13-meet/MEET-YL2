class Animal:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sleep(self):
		print self.name + " is " + str(self.age) + " and is sleeping"

	def eat(self):
		print self.name + " is " + str(self.age) + " and is eating"

class Bird(Animal):
	def __init__(self, wings_color, name, age):
		Animal.__init__(self, name, age)
		self.wings_color = wings_color

	def fly(self):
		print self.name + " is flying with its " + self.wings_color + " wings"



a = Animal("Rami", 1)
a.sleep()
a.eat()

b = Bird("blue", "A_Bird", 10)
b.fly()
b.sleep()
