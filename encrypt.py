#!/usr/bin/env python3

# This program encrypts a specific directory specified by the user.
# The program will automatically generate a decrypt program to decrypt
# the files. Specify a directory when promoted and let it do its magic.
# This will not encrypy directories inside of the directory inputed by the user
# Do not use this for malisous intent.

import os
from cryptography.fernet import Fernet

files = []

print("")
print("Ensure you are not encrpyting important system files")
print("This will generate a decrypt file in the same directory as encrypt")
print("Some directories will not work. ex: / ")
print("")
directory = input("Enter the directory you would like to encrpyt:\t")

try:
	if directory == "/":	#Makes sure its not root directory
		directory / 0

	for file in os.listdir(directory):
		if file == "encrypt.py" or file == "decrypt.key" or file == "decrypt.py":
			continue
		if os.path.isfile(file):
			files.append(file)

	key = Fernet.generate_key()

	with open("decrypt.key", "wb") as decrypt:
		decrypt.write(key)

	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_encrypted = Fernet(key).encrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_encrypted)

	print("All files in %s have been encrypted"% directory)
	print("Files changed: " + str(files)) 
except:
	print("An error occured, likely you entered an invalid directory")
