# Password Strength Calculator

This function rates your password from 1 to 10.
Anton Demkin, 2017
antondemkin@yandex.ru

# Usage:

Before first launch you need to download actual list of worst passwords from [here](https://github.com/danielmiessler/SecLists/tree/master/Passwords)
You need any file, for example 10_million_password_list_top_1000.txt.
Rename it to passwords.txt and place into the same directory as script.

How to run:
```
python3 password_strength.py
```
example:
```
python3 password_strength.py 
Enter password: onion&garlicAREt4sty
10

python3 password_strength.py 
Enter password: monkey1999
5
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
