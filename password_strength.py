import re
import getpass


def get_password_strength(password):
    checklist = [r"(.){5,}",                    # length more than 5, 12 or 20
                 r"(.){12,}",
                 r"(.){20,}",
                 r"\d",                         # contain digit
                 r"[^a-zA-Z0-9]",               # contain special symbol (not letter and not digit)
                 r"[a-z]",                      # contain lowercase letter
                 r"[A-Z]",                      # contain uppercase letter
                 r"^(?!.*(.)\1\1\1\1).*",       # does not contain symbols repeated more than 4 times
                 r"^(?!.*(1|2)(\d)(\d)(\d)).*"] # does not contain a year (four digits, started with 1 or 2)
    
    worst_passwords = load_worst_passwords()
    
    security_levels = []
    
    for regexp in checklist:
        if re.search(regexp, password) is not None:
            security_levels.append(regexp)
    
    if password not in worst_passwords:
        security_levels.append('not in worst')
    
    return len(security_levels)

def load_worst_passwords():
    try:
        with open('passwords1.txt', 'r') as file:
            worst_passwords = file.read()
        return worst_passwords
    except FileNotFoundError:
        print('Please put passwords.txt to script directory. Checking for worst passwords is disabled.')
        return []



def main():
    password = getpass.getpass()
    print(get_password_strength(password))


if __name__ == '__main__':
    main()
