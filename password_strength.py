'''
This script rates your password from 1 to 10.

'''

def get_password_strength(password):
    '''
    This function returns an integer from 1 to 10 depending on a password strength.
    usage: get_password_strength(password)
    '''
    digits = '0123456789'
    special = '!@#$%^&*()_+=-;|/?.,`~][{}/\\ '
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWZYX'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    years = [str(i) for i in range(1900,2017)]
    worst = '123456 password 12345678 qwerty 12345 123456789 football 1234 1234567 baseball welcome 1234567890 abc123 111111 1qaz2wsx dragon master monkey letmein login princess qwertyuiop solo passw0rd starwars'
    
    strength = 0
    
    # check length
    if len(password) > 8:
        strength += 1
    if len(password) > 15:
        strength += 1
    if len(password) > 25:
        strength += 1
    
    # check if password in list of worst
    if password not in worst:
        strength += 1

    # check if there is any year in
    year_in_password = False
    for year in years:
        if year in password:
            year_in_password = True
    if year_in_password == False:
        strength += 1
        
    # check for digits
    for letter in password:
        if letter in digits:
            strength += 1
            break
    
    # check for special letters
    for letter in password:
        if letter in special:
            strength += 1
            break
    
    # check for uppercase
    for letter in password:
        if letter in uppercase:
            strength += 1
            break
    
    # check for lowercase
    for letter in password:
        if letter in lowercase:
            strength += 1
            break
            
    # check for repeating letter
    maxreps = 0
    repeats = 0
    for i in range(0,len(password)):
        for j in range(i+1,len(password)):
            if password[i] == password[j]:
                repeats += 1
            else:
                if maxreps < repeats:
                    maxreps = repeats
                repeats = 0
                continue
    if maxreps < 3:
        strength += 1
        
    # print('reps:', maxreps)
    # print('%s strength: %d' % (password, strength))
    return strength

def test():
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


if __name__ == '__main__':
    pass
