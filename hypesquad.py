import json, requests, colorama, os, sys, time, threading
from os import system
from colorama import *
from pystyle import *

os.system("cls")
system('title Soul Tool - Hypesquad')
print("""
[1]Bravery
[2]Brilliance
[3]Balance
[4]Leave the HypeSquad""")
choice = input("""
[>>>]Select an option:""")

def hype(token):
            headers = {'Authorization' : token}

            if choice == "1":
                housefinal = '1'

            if choice == "2":
                housefinal = '2'

            if choice == "3":
                housefinal = '3'

            if choice == '4':
                housefinal = None

            if choice == '1' or '2' or '3':
                payload = {
                    'house_id': housefinal
                }
                rep = requests.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
                if rep.status_code == 204:
                    print(f'''[>]Done''')
                else:
                    print(f'''[!]Failed, Retrying.''')

            if choice == '4':
                payload = {
                    'house_id': housefinal
                }
                req = requests.delete('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload)
                if req.status_code == 204:
                    print(f'''
[>]Done''')
                    return
                else:
                    pass

            else:
                pass

tokens = open('tokens.txt', 'r').read().splitlines()
for token in tokens:
            threading.Thread(target=hype(token)).start()