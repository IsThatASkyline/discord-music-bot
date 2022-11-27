import discord
from discord.ext import commands
from youtube_dl import YoutubeDL


YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

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
        vc = await ctx.message.author.voice.channel.connect()
    if ctx.author.voice is None:
        return await ctx.send("Ну ты и конченный, сначала надо зайти на канал.")
    elif ctx.guild.voice_client and ctx.voice_client.is_playing() is True:

        with YoutubeDL(YDL_OPTIONS) as ydl:
            if 'https://' in url:
                info = ydl.extract_info(url, download=False)
            else:
                info = ydl.extract_info(f'ytsearch:{url}', download=False)['entries'][0]

        link = info['formats'][0]['url']
        queue.append(link)
        return await ctx.send("Добавил твой трек в очередь")

    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            if 'https://' in url:
                info = ydl.extract_info(url, download=False)
            else:
                info = ydl.extract_info(f'ytsearch:{url}', download=False)['entries'][0]

        link = info['formats'][0]['url']

        vc.play(discord.FFmpegPCMAudio(source=link, **FFMPEG_OPTIONS), after=lambda e: check_queue(ctx, vc))



@bot.command()
async def stop(ctx):
    if bot.guilds:
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Я не в канале, твоя мать в канаве")

bot.run(TOKEN)
