import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import Config

YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)


@bot.command()
async def play(ctx, url):
    if ctx.author.voice is None:
        return await ctx.send("Ну ты и конченный, сначала надо зайти на канал.")
    elif ctx.guild.voice_client:
        return await ctx.send("Уже играет нереальный трек, жди пока он закончится")
    else:
        vc = await ctx.message.author.voice.channel.connect()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            if 'https://' in url:
                info = ydl.extract_info(url, download=False)
            else:
                info = ydl.extract_info(f'ytsearch:{url}', download=False)['entries'][0]

        link = info['formats'][0]['url']

        vc.play(discord.FFmpegPCMAudio(executable='ffmpeg\\ffmpeg.exe', source=link, **FFMPEG_OPTIONS))

@bot.command()
async def stop(ctx):
    if bot.guilds:
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Я не в канале, твоя мать в канаве")

bot.run(Config.token)
