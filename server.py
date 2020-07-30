import discord
from discord.ext import commands
from discord.utils import get

import asyncio
import json
from config import settings

client = commands.Bot(command_prefix = settings['prefix'])
client.remove_command('help')

serverprefix = settings['prefix']
serverbot = settings['bot']
serverid = settings['id']
servertoken = settings['token']
serverpremium = settings['premium']

inviterole = 735998189961740298

print('Connecting to server...')

# start
@client.event
async def on_ready():
    change_status.start()
    channel = bot.get_channel(КАНАЛ КУДА ОТПРАВИТЬ ИНФУ)
    print('Главная часть бота Загружена!')
    embed = discord.Embed(colour=discord.Colour.red())
    embed.set_author(name='Информация')
    embed.add_field(name='`ID:`', value=f'[{serverid}]', inline=False)
    embed.add_field(name='`Title Bot:`', value=f'[{serverbot}]', inline=True)
    embed.add_field(name='`Prefix:`', value=f'[{serverprefix}]', inline=False)
    embed.add_field(name='`Premium Статусов:`', value=f'[{serverpremium}]', inline=False)
    embed.set_footer(text="Статус: `Online`")
    await channel.send(embed=embed)

# endstart

@client.event
async def on_member_join(member):
    role = get(member.guild.roles, id=inviterole)
    pchannel = 738250863742550056
    print(f"Пользователь {member} был приглашен на сервер и ему была выдана роль: \"Unlinked\".\nЧтобы начать с ним общение, необходимо, чтобы он подтвердил свой вход!")
    await member.add_roles(role)
    embed = discord.Embed(colour=discord.Colour.red())
    embed.set_author(name=f'Информация о новом пользователе \"{member}\":')
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name='`ID`', value=member.id)
    embed.add_field(name='`Никнейм:`', value=member.display_name)
    embed.add_field(name='`Создал аккаунт:`', value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name='`Присоединился на сервер:`', value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    await pchannel.send(embed = embed)
    await member.send(f"**Хей {member.mention}, Мы рады тебя видеть!**")
    await member.send("Чтобы начать общение, необходимо, чтобы ты подтвердил свой вход на канале: **#вход**")

client.run(servertoken)
