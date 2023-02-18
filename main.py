import discord, os
from discord.ext import commands
from yt_dlp import YoutubeDL

# YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

access_ids = [763733128438743050, 412625138631049237]

players = {}
queue = []

def check_queue(ctx, vc):
    if queue != []:
        link = queue.pop(0)
        vc.play(discord.FFmpegPCMAudio(source=link, **FFMPEG_OPTIONS),
                after=lambda e: check_queue(ctx, vc))


@bot.command()
async def play(ctx, url):
    vc = ctx.voice_client
    if vc is None:
        try:
            vc = await ctx.message.author.voice.channel.connect()
        except Exception:
            return await ctx.send("Ты пидр")
    if ctx.author.voice is None:
        return await ctx.send("Ты пидр")
    elif ctx.guild.voice_client and ctx.voice_client.is_playing() is True:
        if ctx.message.author.id in access_ids:
            with YoutubeDL() as ydl:
                if 'https://' in url:
                    info = ydl.extract_info(url, download=False)
                else:
                    info = ydl.extract_info(f'ytsearch:{url}', download=False)['entries'][0]
            link = info['formats'][0]['url']
            queue.append(link)
            return await ctx.send("Добавил твой трек в очередь")
        else:
            await ctx.send("Иди нахуй хуесос")
    else:
        if ctx.message.author.id in access_ids:
            with YoutubeDL() as ydl:
                if 'https://' in url:
                    info = ydl.extract_info(url, download=False)
                else:
                    info = ydl.extract_info(f'ytsearch:{url}', download=False)['entries'][0]

            link = info['formats'][0]['url']
            print(link)
            vc.play(discord.FFmpegPCMAudio(source=link, **FFMPEG_OPTIONS), after=lambda e: check_queue(ctx, vc))
        else:
            await ctx.send("Пошел нахуй")


@bot.command()
async def stop(ctx):
    if bot.guilds:
        if ctx.message.author.id in access_ids:
            await ctx.guild.voice_client.disconnect()
        else:
            await ctx.send("Похую")
    else:
        await ctx.send("Иди нахуй")

bot.run(os.getenv('TOKEN'))
