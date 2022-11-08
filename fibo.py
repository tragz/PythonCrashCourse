# Fibonacci numbers module
# A module contains 
#	Executable statments
#	Function Definations

# Each module has its own private namespace
# this namespace is used as global namespace by all functions defined in the module

# modules can import other modules
# all "import" statments need not be at the beginning of a module

# from fibo import *
# imports all names except those beginning with an underscore (__)

# importlib.reload() - reaload the module/restart the interpreter session

def fib(n): # write Fibonacci series up to n
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()


def fib2(n): 	# return Fibonacci series up to n
	result = []
	a, b = 0, 1
	while a<n:
		result.append(a)
		a,b = b, a+b
	return result



if __name__ == "__main__":
	import sys
	fib(int(sys.argv[1]))
	print(fib2(int(sys.argv[1])))