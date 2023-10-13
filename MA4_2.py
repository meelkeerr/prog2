#!/usr/bin/env python3
from numba import njit
from person import Person

def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n - 1) + fib_py(n - 2)

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n - 1) + fib_numba(n - 2)
	
def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print(fib_numba(5))
	

if __name__ == '__main__':
	main()
