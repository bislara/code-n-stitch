from math import log2

def calculate_entropy_string(password: str, range_password=0) -> int:
    if not range_password:
        # calculate range_password of a given password before calculate entropy
        VALUES = {'lower': 26, 'upper': 26, 'int': 10, 'special' : 32}
        check = {'lower': True, 'upper': True, 'int': True, 'special': True}
        
        
        password_set = set(password)
        for char in password_set:
            if char.isalpha():
                if char.islower() and check['lower']:
                    range_password += VALUES['lower']
                    check['lower'] = False
                if char.isupper() and check['upper']:
                    range_password += VALUES['upper']
                    check['upper'] = False
            
            elif char.isnumeric():
                if check['int']:
                    range_password += VALUES['int']
                    check['int'] = False
                
            elif check['special']:
                range_password += VALUES['special']
                check['special'] = False
    
    # expression for calculate entropy
    return round(len(password) * log2(range_password), 2)


def calculate_entropy_diceware(password: str):
    ENTROPY_BY_WORD = 12.92
    lst = password.split()
    return len(lst) * ENTROPY_BY_WORD

if __name__ == '__main__':
    pwd = input('Enter you\'r password: ')
    if len(pwd.split()) > 2:
        entropy = calculate_entropy_diceware(pwd)
    else:
        entropy = calculate_entropy_string(pwd)
    print(f"The password \"{pwd}\" have an entropy of {entropy}")
