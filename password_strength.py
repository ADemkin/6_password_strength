import re
import getpass


def get_password_strength(password):
    checklist = [r"\d",                         # contain digit
                 r"[^a-zA-Z0-9]",               # contain special symbol (not letter and not digit)
                 r"[a-z]",                      # contain lowercase letter
                 r"[A-Z]",                      # contain uppercase letter
                 r"^(?!.*(.)\1\1\1\1).*",       # does not contain symbols repeated more than 4 times
                 r"^(?!.*(1|2)(\d)(\d)(\d)).*"] # does not contain a year (four digits, started with 1 or 2)
    
    with open('worst_passwords.txt', 'r') as file:
        worst_passwords = file.read()
    
    security_levels = []
    
    if len(password) > 5:
        security_levels.append('len5')
    if len(password) > 12:
        security_levels.append('len12')
    if len(password) > 20:
        security_levels.append('len20')
    
    for regexp in checklist:
        if re.search(regexp, password) is not None:
            security_levels.append(regexp)
    
    if password not in worst_passwords:
        security_levels.append('not in worst')
    
    return len(security_levels)


def main():
    password = getpass.getpass()
    print(get_password_strength(password))


if __name__ == '__main__':
    main()
