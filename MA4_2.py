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
	fib_seq = [n for n in range(20, 31)]
	t_py = []
	t_numba = []
	t_cpp = []
	
	
	for n in range(20, 31):
		start = pc()
		fib_py(n)
		end = pc()
		t_py.append(end - start)

	
	for n in range(20, 31):
		start = pc()
		fib_numba(n)
		end = pc()
		t_numba.append(end - start)
	p = Person(1)
	
	for n in range(20, 31):
		start = pc()
		p.set(n)
		p.fib()
		end = pc()
		t_cpp.append(end - start)
	
	
	plt.plot(fib_seq, t_py, label='python')
	plt.plot(fib_seq, t_numba, label='numba')
	plt.plot(fib_seq, t_cpp, label='C++')
	plt.grid()
	plt.xlabel('n')
	plt.ylabel('Time (s)')
	plt.legend()
	plt.savefig('ma4_2.png')
	print(fib_numba(47))
	p.set(47)
	print(p.fib())

	
			

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return (fib_numba(n - 1) + fib_numba(n - 2))

if __name__ == '__main__':
	main()
