import os

def encrypt(text,s): 
	result = "" 

	# traverse text 
	for i in range(len(text)): 
		char = text[i]  
		result += chr((ord(char) + s - 32) % 95 + 32) 
	return result 

def decrypt(text,s): 
	result = "" 

	# traverse text 
	for i in range(len(text)): 
		char = text[i]  
		result += chr((ord(char) - s - 32) % 95 + 32) 
	return result

if __name__ == "__main__":
	while (True):
		print('Select : ')
		print('1. Encrypt ')
		print('2. Decrypt ')
		print('0. Exit ')
		ans = int(input('Your answer : '))
		if(ans == 1):
			text = input("Input plain text : ")
			s = int(input("Input shift : ")) 
			print ("Ciphertext : " + encrypt(text,s))
		elif(ans == 2):
			text = input("Input plain text : ")
			s = int(input("Input shift : ")) 
			print ("Plaintext : " + decrypt(text,s))
		elif(ans == 0):
			break
		os.system('pause')
		os.system('cls')