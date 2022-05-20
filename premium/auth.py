from unittest import result
import discord
from discord.ext import commands
import random
import asyncio
from discord.ext import commands
import time
from discord import Permissions
from colorama import Fore, Style
import subprocess, requests, time, os
def check():
    global res
    global lol
    res = 4

    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    r = requests.get('https://pastebin.com/raw/fK6fu6m7') # Paste your URL  e.g(https://pastebin.com)

    try:
        check = r.text
        if hwid in check:
            res = 1
            pass
        else:
            res = 0
    except:
        
        print("[ERROR] Failed to connect to database")
        time.sleep(5)  
        res = 2
    
    lol = 2
    return res

def check2():
    if res != 1:
        if lol == 2:
            wow = 1 
            return wow
def hwid():
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    return hwid
