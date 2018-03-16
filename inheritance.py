class Animal(object):
	def run(self):
		print('Animal is running')
class Dog(Animal):
	def run(self):
		print('Dog is running')
class Cat(Animal):
	def run(self):
		print('Cat is running')
dog=Dog()
dog.run()
cat=Cat()
cat.run()#son's run() covers father's run()
print('------------------')
a=isinstance(dog,Animal)
print(a)
b=isinstance(dog,Dog)
print(b)
c=isinstance(Animal(),Dog)
print(c)#son from father,father not from son
def run_twice(Animal):
	Animal.run()
	Animal.run()
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())


class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly')
run_twice(Tortoise())#zhiguandiaoyong,don't care details 
#open&close:open sons,close functions on father 
#python felt like object
class Timber(object):
	def run(self):
		print('Start...')
run_twice(Timber())#only if you have class-function-run(),you don't have to care about whether the class is son of Animal
