import discord,asyncio,aiohttp,json
from discord import Webhook
from discord.ext import commands
from operator import iadd
from discord.utils import get 
from discord.commands import Option,slash_command



bot = commands.Bot(command_prefix="!" , intents=discord.Intents.all()) 


#上線回應
@bot.event
async def on_ready():
    print("本開源由 我是人#8315 製作")
    print("請勿修改")
    print("有問題請至 https://discord.gg/WDxmw5WjPY 詢問")
    print("==================================================")
    print(F"{bot.user}已連線")
    activity=discord.Activity(type=discord.ActivityType.watching, name="一款好用的webhook發送器") #更改狀態
    await bot.change_presence(status=discord.Status.dnd,activity=activity)


#webhook功能
@slash_command()
@bot.slash_command(name="webhooksend",description="Webhook發送功能")
async def webhooksend(ctx,url,username,*,msg):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(F"{url}", session=session)
        await webhook.send(F"{msg}", username=F"{username}")  
        await ctx.respond("發送成功",ephemeral=True)




bot.run("TOKEN")#放上token
