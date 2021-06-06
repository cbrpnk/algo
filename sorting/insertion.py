#!/bin/python

def sort(data):
	for i in range(1, len(data)):
		j=i
		while j>0 and data[j] < data[j-1]:
			data[j], data[j-1] = data[j-1], data[j]
			j -= 1
	

if __name__ == "__main__":
	data = [1, 5, 7, 3, 5, 9, 1, 4, 7, 4, 2, 6, 8, 9, 1, 4, 2, 5, 7, 3, 8, 9]
	sort(data)
	print(data)
	
