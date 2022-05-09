import re

emailpattern = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
pw = re.compile(r"[a-zA-Z0-9-$%#@]{8,}\d$")
string = 'mail@gmail.com'
passw = '01234$67asas9'
a = emailpattern.search(string)
check = pw.search(passw)
print(check)
# correo = input('Write your email: ')
# passw= input('Write your password: ')


'''
Password requirements 
1) At least 8 characters long
2) can contain any sort of letters-numbers-$%#@
'''
