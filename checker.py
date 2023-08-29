from requests import get, post
from random import randint
from pystyle import *
import os, sys

os.system("cls")
def variant1(token):
    response = get('https://discord.com/api/v9/auth/login', headers={"Authorization": token})#Bad variant for mass token check due to the rate limit.
    return True if response.status_code == 200 else False

def variant2(token):
    response = post(f'https://discord.com/api/v9/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def variant2_Status(token):
    response = post(f'https://discord.com/api/v9/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'

if __name__ == "__main__":
    try:
        checked = []
        with open('tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and variant2(token) == True:
                    print(f'''
[+]Token: {token} | Valid Token''')
                    checked.append(token)
                else:
                    print(f'''
[+]Token: {token} | Invalid Token''')
        if len(checked) > 0:
            save = input(f'''
{len(checked)} valid tokens founded!\nDo you want to save the valid tokens in the file "valid.txt" (y/n)''')
            if save == 'y':
                name = open("valid.txt")
                with open(f'valid.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                print(f'I have succesfully saved the valid tokens to valid.txt File!')
        input('''
[>>]Press Enter For Exit...''')
    except:
        input('''
[+]Unknow error, you are probably offline. Press ENTER to exit:''')
       