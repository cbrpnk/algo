#!/bin/python

if __name__ == "__main__":
	m = 2**31-1
	a = 7**5
	x = 1047
	for i in range(0, 1000):
		x = (a * x) % m
		print(x/m)
