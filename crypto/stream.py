#!/bin/python

import math
import prng.lehmer as lehmer

if __name__ == "__main__":
	plaintext = bytearray(b"This is a test")
	cyphertext = bytearray()
	
	for c in plaintext:
		r = math.floor(lehmer.rand() * 256) 
		cyphertext.append(c ^ r)
	
	print(plaintext)
	print(cyphertext)
