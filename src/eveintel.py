import asyncio
import os
import glob
import discord

#directory that contains chatlogs. default is for linux/proton version
default_linux_dir = '/home/user/.steam/steam/steamapps/compatdata/8500/pfx/drive_c/users/steamuser/My Documents/EVE/logs/Chatlogs/'
#chatlogs_dir = os.environ['chatlogs_dir']
#change this to reflect the location of your chatlogs
chatlogs_dir = default_linux_dir
#discord token - check here: https://discord.com/developers/applications
#discord_token = os.environ['discord_token']
discord_token = os.environ['discord_token']
#Channel id to forward chat to. On discord, right click channel, Copy ID.
#notifications_chan_id = os.environ['notifications_chan_id']
notifications_chan_id = 9999999999999999
#name of the EVE Online channel. Default is local system chat.
#chankeyword = os.environ['chankeyword']
chankeyword = 'Local'

#initiate discord vars
client = discord.Client()
###intents api update. if you use the reworked discord api and intents in your bot, uncomment the next 2 lines.
#intents = discord.Intents().all()
#client = discord.Client(prefix='', intents=intents)

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