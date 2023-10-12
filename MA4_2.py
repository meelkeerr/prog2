#!/usr/bin/env python3
from numba import njit
from person import Person

def fib_py(n):
	pass

@njit
def fib_numba(n):
	pass
	
def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())

if __name__ == '__main__':
	main()
