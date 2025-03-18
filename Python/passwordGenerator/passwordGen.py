import sys
import random
import array

def main(mylen):
	
	mymax = 20
	mymin = 8
	if mylen < mymin or mylen > mymax:
		print("nope, try again")
	else:
		DIGITS = ['0','1','2','3','4','5','6','7','8','9']
		lowercaseLetter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
						 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
						 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
						 'z']

		upercaseLetter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

		myCharacters = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
						'*', '(', ')', '<']

		allComb = lowercaseLetter + upercaseLetter + myCharacters
		randDigit = random.choice(DIGITS)
		randLower = random.choice(lowercaseLetter)
		randUpper = random.choice(upercaseLetter)
		randChar = random.choice(myCharacters)
		tempPass = randDigit + randLower + randUpper + randChar
		

		for x in range(mylen - 4):
			tempPass = tempPass + random.choice(allComb)
			tempPassList = array.array('u', tempPass)
			random.shuffle(tempPassList)
		
		password = ''
		for x in tempPassList:
			password = password + x
		print(password)

main(int(sys.argv[1]))
