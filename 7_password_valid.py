import re
password= input("Enter your password:   ")
t = True
while t:  
    if (len(password)<=6 or len(password)>=16):
        break
    elif not re.search(r"[a-z]",password):
        break
    elif not re.search(r"[0-9]",password):
        break
    elif not re.search(r"[A-Z]",password):
        break
    elif not re.search(r"""[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]""",password):
        break
    elif re.search(r"\s",password):
        break
    else:
        print("Valid Password")
        t= False
        break

if t:
    print("Not a Valid Password")
