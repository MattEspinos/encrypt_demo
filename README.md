# Directory Encryption Tool
This tool encrypts all files in a specified directory using the Fernet symmetric encryption algorithm. The tool generates a key file and saves it in the same directory as the encrypted files. To decrypt the files, you need the key file and the decrypt program, which the tool also generates.

## Installation
This tool requires Python 3 and the cryptography library. You can install the library using pip:
```
pip install cryptography
```
## Usage
- To encrypt a directory, run the encrypt.py script and provide the directory path when prompted:

```
python encrypt.py
```
- Enter the directory you would like to encrypt: /path/to/directory
The tool will encrypt all files in the directory and save the key file (decrypt.key) and decrypt program (decrypt.py) in the same directory. The tool skips the encrypt.py, decrypt.py, and decrypt.key files to avoid encrypting them.

### To decrypt the files, run the decrypt.py script and provide the key file path when prompted:

```
python decrypt.py
```
- Enter the key file path: /path/to/directory/decrypt.key
The tool will decrypt all encrypted files in the directory and save them with the .decrypted extension.

## Limitations
The tool only encrypts files in the specified directory, not subdirectories.
The tool may not work on some directories, such as the root directory (/).
Use this tool responsibly and only for legitimate purposes. Do not use it for malicious intent.
## License
This tool is licensed under the MIT License. See the LICENSE file for more information.