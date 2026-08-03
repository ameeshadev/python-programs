program to define 4 private instance variable values and print outside of that class
class A:
    def __init__(self,name,age,roll,branch):
	self.__name=name
	self.__age=age
	self.__roll=roll
	self.__branch=branch
    def display(self):
	return self.__name,self.__age,self.__roll,self.__branch
obj=A()
name,age,roll,branch=obj.display()
print(name,age,roll,branch)
