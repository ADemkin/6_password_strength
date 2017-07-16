'''
This script rates your password from 1 to 10.

'''
from collections import Counter
import string

def get_password_strength(password):
    '''
    This function returns an integer from 1 to 10 depending on a password strength.
    usage: get_password_strength(password)
    '''
    #checklist = [string.digits, string.punctuation, string.ascii_lowercase, string.ascii_lowercase]
    years = [str(i) for i in range(1900,2017)]
    worst = '123456 password 12345678 qwerty 12345 123456789 football 1234 1234567 baseball welcome 1234567890 ' \
            'abc123 111111 1qaz2wsx dragon master monkey letmein login princess qwertyuiop solo passw0rd starwars'
    
    password_strength = set()
    
    # check length
    if len(password) > 8:
        password_strength.add('len8')
    if len(password) > 15:
        password_strength.add('len15')
    if len(password) > 25:
        password_strength.add('len25')
    
    # check if password in list of worst
    if password not in worst:
        password_strength.add('password not in list of worst passwords')

    # check if there is any year in
    year_in_password = False
    for year in years:
        if year in password:
            year_in_password = True
    if year_in_password == False:
        password_strength.add('no year in password')
        
    # (devman) simplify:
    for letter in password:
        if letter in string.digits:
            password_strength.add('digit')
        if letter in string.punctuation:
            password_strength.add('special symbol')
        if letter in string.ascii_uppercase:
            password_strength.add('uppercase')
        if letter in string.ascii_lowercase:
            password_strength.add('lowercase')
   
            
    # check for repeating letter
    repeats = Counter(password)
    max_repeats = max(repeats.values())
    if max_repeats < 5:
        password_strength.add('no repeated symbols')
    
    # print('%s strength: %d' % (password, strength))
    return len(password_strength)

def main():
    # check passwords
    print(get_password_strength('aaabc') )
    print(get_password_strength('Abc'))
    print(get_password_strength('Abc1'))
    print(get_password_strength('Abc1dgefh'))
    print(get_password_strength('Abc1dgefh$#'))
    print(get_password_strength('Abc1dgefh$#hgydaaaaa'))
    print(get_password_strength('12345678'))
    print(get_password_strength('monkey'))
    print(get_password_strength('qwertyuiop'))
    print(get_password_strength('1987'))
    print(get_password_strength('1987a'))
    print(get_password_strength('1987aA'))
    print(get_password_strength('1987a A'))
    print(get_password_strength('ah83H8hfs h78h2m87hm87asf29ma hjkdsfh782mhx98hsfho '))
    print(get_password_strength('aaaaab5'))
    print(get_password_strength('5555555555'))
    print(get_password_strength('abcdefghijklmnOPQ73615409836rstu ^&*!$%)( xyz'))

if __name__ == '__main__':
    main()
