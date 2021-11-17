import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print(' [!] Started Dmming Ids\n')

    with open("ids.json", "r") as file:
        data = json.load(file)
    with open("config.json", "r") as message:
        m = json.load(message)
        message = m["message"]
    indx = 0
    for i in data:
        indx += 1
        member = await bot.fetch_user(i)
        try:
            await member.send(str(message))
            print(f" [+] Sent message {indx} / {len(data)}")
        except Exception as e:
            print(f" [!] {e}")

    print(" [+] Done")

with open("config.json", "r") as config:
    get = json.load(config)
    auth = get["token"]

print(auth)
bot.run(auth, bot = False)
