# Encrpytion Tool
A basic CLI Python based tool for encrypting and decrypting multiple famous algorithms and cipher such as: 
* Base64
* Morse
* Caesar Cipher
* Hex

## Known Errors:
* Caesar Cipher Decryption Brute Force isn't working properly. It's known, I am working really hard on this.

## Required Dependencies:
* Base64, It's always better to check that you actually have that installed using: 
```bash
python -m pip install base64
```
* Binascii, I am not quite sure if it comes with stock python so run this command:
```bash
python -m pip install binascii
```
* Morse3, DOESN'T come with stock python, Install it using:
```bash
python -m pip install morse3
```

## Required Python Version:
This was built using Python 3.8.3, It's recommended to use the same version, but you can use anything higher than 3.6 and lower than 3.9 (I haven't tested it yet on 3.9)

## Usage:
After you installed everything required, Run the following command:
```bash 
python enc.py
```
And follow the instructions.

## Some important notes:
If you want to decrypt from Caesar Cipher, You can't enter the key, The program will just run every key until 25. It will be fixed next version.

## Made By Max Iliocuhenko: [My Github](https://github.com/maxily1)

