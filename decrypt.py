#!/usr/bin/env python3

# This program encrypts a specific directory specified by the user.
# The program will automatically decrypt the files in a given directory

import os
from cryptography.fernet import Fernet

files = []

print("Ensure the decrypt.key file is in the same directory as decrypy.py")
print("")
directory = input("Enter the directory you would like to decrypt:\t")

try:
	if directory == "/":	#Makes sure its not root directory
		directory / 0

	for file in os.listdir(directory):
		if file == "encrypt.py" or file == "decrypt.key" or file == "decrypt.py":
			continue
		if os.path.isfile(file):
			files.append(file)

	with open("decrypt.key", "rb") as key:
		fileskey = key.read()

	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(fileskey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)

	print("Successfully decrypted files in %s"% directory)
except:
	print("An error occured, likely you entered an invalid directory")
