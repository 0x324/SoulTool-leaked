import threading, time, os, requests, json, sys, colorama
from os import system
from colorama import *
from pystyle import *


os.system("cls")
system("title Soul Tool - NickName Changer")
def changenick(server, nickname, token):
            headers = {'Authorization' : token}

            r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                               json={"nick": nickname})
            if r.status_code == 200:
                print(f'''
[>]Nickname Changed Succesfully!''')
            elif r.status_code != 200:
                print(f'''
[-]Error, Cant Change Nickname...''')

tokens = open('tokens.txt', 'r').read().splitlines()
server = input("Server ID:")
nick = input("Nickname:")
for token in tokens:
  threading.Thread(target=changenick, args=(server, nick, token)).start()
input("""
[>]Press ENTER to exit:""")

