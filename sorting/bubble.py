#!/bin/python

def sort(data):
	for i in range(0, len(data)-1):
		for j in range(0, len(data)-i-1):
			if(data[j] > data[j+1]):
				data[j], data[j+1] = data[j+1], data[j]
			
	

if __name__ == "__main__":
	data = [1, 5, 7, 3, 5, 9, 1, 4, 7, 4, 2, 6, 8, 9, 1, 4, 2, 5, 7, 3, 8, 9]
	sort(data)
	print(data)
	
