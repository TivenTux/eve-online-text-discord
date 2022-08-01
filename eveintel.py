import requests
import os
import json, re 
import time
import discord, time, os, random, requests, json
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio, urllib, urllib.request, subprocess, sys 
import glob

globdir = '/home/user/.steam/steam/steamapps/compatdata/8500/pfx/drive_c/users/steamuser/My Documents/EVE/logs/Chatlogs/'
token = 'xxxxxxxxxxxxxxxxxxxxxx'
notifications_chan_id = 999999999999999999
chankeyword = 'Local'

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as', client.user.name)
    await background_loop()

async def background_loop():
    #find channel's log and sort by date
    globby = sorted(glob.glob(globdir + str(chankeyword) + '*.txt'), key=os.path.getmtime)
    #print(len(globby))
    #find last edited
    lenglobby = len(globby)
    cl2 = lenglobby - 1
    chatlog = globby[cl2]
    notifications_chan = client.get_channel(notifications_chan_id)
    tnum = 0
    previous_line = ''
    while True:
        with open(chatlog,'r', encoding='utf-16-le') as f:
            for line in f:
                pass
            last_line = line
            
            if str(last_line) != str(previous_line) and tnum > 0:
                print(last_line)
                await notifications_chan.send(last_line)
            previous_line = last_line
        tnum += 1
        await asyncio.sleep(0.6)


def Main():
    client.run(token)   
    
if __name__ == "__main__":

    Main()