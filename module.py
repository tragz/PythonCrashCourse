import fibo as fib

if __name__ == "__main__":
	import sys
	fib.fib(int(sys.argv[1]))
	print(fib.fib2(int(sys.argv[1])))