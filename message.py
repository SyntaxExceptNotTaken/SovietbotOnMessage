import discord
import traceback
import psutil
import os
import random
import asyncio

from datetime import datetime
from discord.ext.commands import errors
from utils import default

class message:
    def __init__(self, bot):
        self.bot = bot

async def on_message(message):
    #checkifmessage.idisbotid
    lowermessage = message.content.lower():
    if "<@482271178015375370>" in lowermessage:
        if "sing" in lowermessage:
            await ctx.send("Союз нерушимый республик свободны/nСплотила навеки Великая Русь./nДа здравствует созданный волей народов/nЕдиный, могучий Советский Союз!")
    if "what am i" in lowermessage:
        choice = random.choice(["very gay", "straight", "a furry", "a My Little Pony fan", "potentially a professional sumo wrestler", "retarded", "not a communist", "a communist"])
        msg = ('You are'+choice+'!')
        msgformat = "{0}".format(msg)
        await ctx.send(msgformat)
    if "i like" in lowermessage:
        if "vodka" in lowermessage:
            await ctx.send("You are a true communist!")
        else:
            userid = ctx.message.author.id
            strid = str(userid)
            await ctx.send("<@"+strid+">, vodka is better.")
    if "communism" in lowermessage:)
            await ctx.send(":Communism:")
            print("hello")
            #FILE PATH NEEDED NEXT LINE
            try:
                file = open(("FILEPATH/communists.txt"), "x")
            except FileExistsError:
                print("yeet, communists are here")
            else:
                #FILE PATH NEEDED NEXT LINE
                file = open("filepathhere/communists.txt", "r+")
            fileread = file.read()
            print(fileread)
            print(message.author.id)
            pinguserid = message.author.id
            if pinguserid in fileread:
                print("work now plz")
                print(fileread)
                try:
                     #FILE PATH NEEDED NEXT LINE
                    rewrite = open(("FILEPATH/"+pinguserid+"communists.txt"), "x")
                    print("big gay")
                except FileExistsError:
                    print("gay2")
                else:
                    #FILE PATH NEEDED NEXT LINE
                    rewrite = open(("FILEPATH/"+pinguserid+"communists.txt"), "x")
                    rewrite(close)
                #FILE PATH NEEDED NEXT LINE
                rewrite = open(("FILEPATH/"+pinguserid+"communists.txt"), "r+")
                pinged = rewrite.read()
                print("test"+pinged)
                if pinged == "":
                    print("gay")
                    rewrite.close()
                    #FILE PATH NEEDED NEXT LINE
                    rewrite = open(("FILEPATH/"+pinguserid+"communists.txt"), "w")
                    rewrite.write("0")
                print("="+pinged+"=")
                rewrite.close()
                #FILE PATH NEEDED NEXT LINE
                rewrite = open(("FILEPATH/"+pinguserid+"communists.txt"), "r+")
                pinged = rewrite.read() 
                print(pinged)   
                pinged = int(int(pinged)+1)
                rewrite.close()
                #FILE PATH NEEDED NEXT LINE
                rewrite = open(("FILEPATH/"+pinguserid+"communists.txt"), "w")
                pinged = str(pinged)
                print(pinged)
                rewrite.write(pinged)
                if int(pinged) >= 10:
                    print("Yes!")
                    print(test)
                    await ctx.send("YOU ARE A TRUE COMRADE"))
                    rewrite.close()
                    #FILE PATH NEEDED NEXT LINE
                    rewrite = open(("FILEPATH/"+pinguserid+"communists.txt"), "w")
                    rewrite.write("0")
                    rewrite.close()
                    file.close()
                file.close()
            else:
                file.close()
                #FILE PATH NEEDED NEXT LINE
                file = open("filepathhere/communists.txt", "a")
                file.write(pinguserid)
    if "duck" in lowermessage:
        await ctx.send("Goose")
def setup(bot):
    bot.add_cog(message(bot))
