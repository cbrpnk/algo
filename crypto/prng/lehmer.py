#!/bin/python

m = 2**31-1
a = 7**5
x = 1047

def rand():
	global x
	x = (a * x) % m
	return x/m

if __name__ == "__main__":
		print(rand())
