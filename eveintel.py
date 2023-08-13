import requests, asyncio, urllib, urllib.request, subprocess, sys, os, re, time, json, random, glob
import discord
from discord.ext.commands import Bot
from discord.ext import commands

#directory that contains chatlogs. default is for linux/proton version
chatlogs_dir = '/home/user/.steam/steam/steamapps/compatdata/8500/pfx/drive_c/users/steamuser/My Documents/EVE/logs/Chatlogs/'
#discord token - check here: https://discord.com/developers/applications
discord_token = 'xxxxxxxxxxxxxxxxxxxxxx'
#Channel id to forward chat to. On discord, right click channel, Copy ID.
notifications_chan_id = 999999999999999999
#name of the EVE Online channel. Default is local system chat.
chankeyword = 'Local'

#initiate discord vars
client = discord.Client()

#when bot gets ready, start the loop
@client.event
async def on_ready():
    print('Logged in as', client.user.name)
    await background_loop()

#main loop
async def background_loop():
    #find channel's log and sort by date
    globby = sorted(glob.glob(chatlogs_dir + str(chankeyword) + '*.txt'), key=os.path.getmtime)
    #find last edited
    lenglobby = len(globby)
    cl2 = lenglobby - 1
    chatlog = globby[cl2]
    #get forwarding channel id from options
    notifications_chan = client.get_channel(int(notifications_chan_id))
    tnum = 0
    previous_line = ''
    while True:
        #definitely use utf-16-le for eve online chat logs
        with open(chatlog,'r', encoding='utf-16-le') as f:
            for line in f:
                pass
            last_line = line
            
            if str(last_line) != str(previous_line) and tnum > 0:
                print(last_line)
                await notifications_chan.send(last_line)
            previous_line = last_line
        tnum += 1
        #small cooldown
        await asyncio.sleep(0.6)


def Main():
    client.run(discord_token)   
    
if __name__ == "__main__":

    Main()