import requests, time, json, sys, os, threading
from os import system
from pystyle import *
from colorama import *

os.system("cls")
os.system("soul tool - Friend Request Spammer")
def friender(token, user):
            try:
                user = user.split("#")
                headers = {'Authorization' : token}
                payload = {"username": user[0], "discriminator": user[1]}
                src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers,
                                    json=payload)
                if src.status_code == 204:
                    print(f"""
[+]Friend Request Sent to {user[0]}#{user[1]} |  {token}""")
            except:
                print(f"""
[-]Error | {token}""")

user = input(f"Input the Username + Tag, (Example:.exe#5257): ")
tokens = open("tokens.txt", "r").read().splitlines()
for token in tokens:
            threading.Thread(target=friender, args=(token, user)).start()
input("[>]Done, Press enter to exit:")




