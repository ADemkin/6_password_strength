# Password Strength Calculator

This function rates your password from 1 to 10.
Anton Demkin, 2017
antondemkin@yandex.ru

# Usage:

Script require internet connection.
It will automatically download [this](https://github.com/danielmiessler/SecLists/blob/master/Passwords/10_million_password_list_top_1000.txt)
list of internet worst passwords. If unable to download (no internet...) it will skip this step and still run.

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
