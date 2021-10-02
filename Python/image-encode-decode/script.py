import sys
import os
import base64
import random

# convert image to string
def img_to_str(img_path):
	with open(img_path, "rb") as image_file:
		img_string = base64.b64encode(image_file.read())
	return img_string

# encode string
def encode_str(img_string):
	key = random.randint(1, 10000)
	img_string = img_string.decode()
	cipher = ' '.join([str(ord(char)^key) for char in img_string])
	return (cipher, key)

# decode string
def decode_str(cipher, key):
	plaintext = ''.join([chr(int(char)^key) for char in cipher.split()]).encode('utf-8')
	return plaintext

# convert string to image
def str_to_img(img_string, img_path):
	with open(img_path, "wb") as image_file:
		image_file.write(base64.b64decode(img_string))
	print(f'Decrypted image stored in {img_path} file in the current directory')

# option to save cipher and key in a text file
def save_files(cipher, key):
	z = input("Press 1 to save the key, any other key to skip: ")
	if z == '1':
		store_in_file('key', str(key))
		print('Key stored in \'key.txt\' file in the current directory')
	else:
		pass
	store_in_file('encrypted_img', cipher)
	print('Encrypted image stored in \'encrypted_img.txt\' file in the current directory')

# write into file
def store_in_file(filename, text):
	with open(f'{filename}.txt', "w") as file:
		file.write(text)

def get_from_file(filename):
	filename = filename.split('.')[0]
	if not os.path.exists(f'{filename}.txt'):
		print(f'{filename}.txt file not found')
		sys.exit()
	with open(f'{filename}.txt', "r") as file:
		text = file.read()
	return text

def option_for_input(param):
	if param == 'cipher':
		z = '1'
	else:
		z = input(f'Press 1 to retrive {param} from file, any other key to enter {param} manually: ')
	if z == '1':
		filename = input(f'Enter filename for {param}: ')
		return get_from_file(filename)
	else:
		return input(f'Enter {param}: ')

if __name__ == '__main__':

	# switching to current running python files directory
	# os.chdir('/'.join(__file__.split('/')[:-1]))
	
	x = input("Press 1 to encrypt, 2 to decrypt: ")
	if x != '1' and x != '2':
		print("Invalid input\nTerminating process")
		sys.exit()

	if x == '1':
		img_path = input("Enter image filename: ")
		if not os.path.isfile(img_path):
			print("File not found\nTerminating process")
			sys.exit()
		cipher, key = encode_str(img_to_str(img_path))
		# print(f'Image encryption: {cipher}\nKey: {key}')
		print(f'Key: {key}')
		save_files(cipher, key)
	
	else:
		cipher = option_for_input('cipher')
		key = option_for_input('key')
		img_string = decode_str(cipher, int(key))
		ext = input('Enter file extension for image (png/jpeg/jpg/): ')
		str_to_img(img_string, f'decrypted_img.{ext}')