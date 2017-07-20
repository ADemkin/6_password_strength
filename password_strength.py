'''
string is nice, but re is better! :-)
'''

import re


def get_password_strength(password):
    # checklist:
    # len8   (.){8,}
    # len15  (.){15,}
    # len25  (.){25,}
    # worst - string only :-/
    # not years  "^(?!.*(1|2)(\d)(\d)(\d)).*"
    # digit  \d
    # special    [^a-zA-Z0-9]
    # uppercase  [A-Z]
    # lowercase  [a-z]
    # NO repeated symbols   ^(?!.*(.)\1\1\1\1).*
    
    checklist = [r"(.){5,}", r"(.){12,}", r"(.){20,}", r"\d", r"[^a-zA-Z0-9]", r"[a-z]", r"[A-Z]",
                 r"^(?!.*(.)\1\1\1\1).*",
                 r"^(?!.*(1|2)(\d)(\d)(\d)).*"]
    worst_passwords = '123456 password 12345678 qwerty 12345 123456789 football 1234567 baseball welcome 1234567890 ' \
            'abc123 111111 1qaz2wsx dragon master monkey letmein login princess qwertyuiop solo passw0rd starwars'
    
    security_levels = set()
    
    for regexp in checklist:
        if re.search(regexp, password) is not None:
            security_levels.add(regexp)
    
    if password not in worst_passwords:
        security_levels.add('not in worst')
    
    return len(security_levels)


def main():
    password = input('Enter password: ')
    print(get_password_strength(password))


if __name__ == '__main__':
    main()
