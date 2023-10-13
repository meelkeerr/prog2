#!/usr/bin/env python3
from matplotlib import pyplot as plt
from numba import njit
from person import Person
from time import perf_counter as pc
from time import sleep as pause

def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n - 1) + fib_py(n - 2)

def main():
	fib_seq = [fib_numba(n) for n in range(20, 31)]
	t_py = []
	t_numba = []
	t_cpp = []
	
	start = pc()
	for n in range(20, 31):
		fib_py(n)
		end = pc()
		t_py.append(end - start)

	start = pc()
	for n in range(20, 31):
		fib_numba(n)
		end = pc()
		t_numba.append(end - start)
	p = Person(1)
	start = pc()
	for n in range(20, 31):
		p.set(n)
		p.fib()
		end = pc()
		t_cpp.append(end - start)
		
	
	plt.plot(t_py, fib_seq, label='python')
	plt.plot(t_numba, fib_seq, label='numba')
	plt.plot(t_cpp, fib_seq, label='C++')
	plt.grid()
	plt.legend()
	plt.savefig('ma4_2.png')

	
			

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return (fib_numba(n - 1) + fib_numba(n - 2))

if __name__ == '__main__':
	main()
