#!/bin/python

def vigenere_enc(key, message):
	key_counter = 0;
	cyphertext = bytearray(len(message))
	
	for i in range(0, len(message)):
		cyphertext[i] = (message[i] + key[key_counter]) % 256
	
	return cyphertext


def vigenere_dec(key, message):
	key_counter = 0;
	cyphertext = bytearray(len(message))
	
	for i in range(0, len(message)):
		cyphertext[i] = (message[i] - key[key_counter]) % 256
	
	return cyphertext

'''
	TODO Do cryptanalysis
'''

if __name__ == "__main__":
	message = bytearray(b"Hi this is a plaintext")
	key = bytearray(b"secret")
	
	print(vigenere_dec(key, vigenere_enc(key, message)))
