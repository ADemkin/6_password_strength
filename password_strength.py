import re
import getpass
import urllib.request
import ssl


def get_password_strength(password):
    checklist = [r"(.){5,}",  # length more than 5, 12 or 20
                 r"(.){12,}",
                 r"(.){20,}",
                 r"\d",  # contain digit
                 r"[^a-zA-Z0-9]",  # contain special symbol (not letter and not digit)
                 r"[a-z]",  # contain lowercase letter
                 r"[A-Z]",  # contain uppercase letter
                 r"^(?!.*(.)\1\1\1\1).*",  # does not contain symbols repeated more than 4 times
                 r"^(?!.*(1|2)(\d)(\d)(\d)).*"]  # does not contain a year (four digits, started with 1 or 2)
    
    worst_passwords = download_worst_passwords()
    
    security_levels = []
    
    for regexp in checklist:
        if re.search(regexp, password) is not None:
            security_levels.append(regexp)
    
    if password not in worst_passwords:
        security_levels.append('not in worst')
    
    return len(security_levels)


def download_worst_passwords():
    try:
        context = ssl._create_unverified_context()
        url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords' \
              '/10_million_password_list_top_10000.txt'
        content = urllib.request.urlopen(url, context=context)
        list_of_passwords = str(content.read())
        
    except urllib.error.HTTPError as error:
        print("Failed to fetch passwords list:", error)
        list_of_passwords = []
        
    finally:
        return list_of_passwords


def main():
    password = getpass.getpass()
    print(get_password_strength(password))


if __name__ == '__main__':
    main()
