from random import randint

import discord
from discord import Embed, ApplicationContext
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="ping", description="ping бота")
    async def ping(self, ctx: ApplicationContext):
        await ctx.respond('Pong! {0}ms'.format(round(self.bot.latency * 1000)))

    @discord.slash_command(name="help", description="Show help message")
    async def help(self, ctx: ApplicationContext):
        help_embed = Embed(
            color=0x11FF11,
            title="Help",
            description="`/ping` - Пинг бота\n"
                        "`/ip` - IP сервера\n"
                        "`/contacts` - Контакты\n"
                        "`/map` - Карты миров сервера\n"
                        "`/vote` - Голосовать за сервер\n"
                        "`/random` - Случайное число от a до b"
        )
        await ctx.respond(embed=help_embed)

    @discord.slash_command(name="ip", description="Отправляет IP сервера")
    async def ip(self, ctx: ApplicationContext):
        ip_embed = Embed(
            color=0x11FF11,
            title="IP DreamMC",
            description="`dreammc.su` (Проски)"
        )
        await ctx.respond(embed=ip_embed)

    @discord.slash_command(name="contacts", description="Отправляет контакты")
    async def contacts(self, ctx: ApplicationContext):
        contacts_embed = Embed(
            color=0x11FF11,
            title="Контакты",
            description="Сайт: https://dreammc.su/\n"
                        "ВКонтакте: https://vk.dreammc.su/\n"
                        "Discord: https://discord.dreammc.su/"
        )
        await ctx.respond(embed=contacts_embed)

    @discord.slash_command(name="map", description="Отправляет ссылки на карты сервера")
    async def map(self, ctx: ApplicationContext):
        map_embed = Embed(
            color=0x11FF11,
            title="Карта",
            description="Мир построек: https://build.dreammc.su\n"
                        "Мир ферм: https://farm.dreammc.su"
        )
        await ctx.respond(embed=map_embed)

    @discord.slash_command(name="vote", description="Проголосовать за сервер")
    async def vote(self, ctx: ApplicationContext):
        vote_embed = Embed(
            color=0x11FF11,
            title="Голосовать",
            url="https://minecraftrating.ru/vote/83916/",
            description="Голосовать за сервер"
        )
        await ctx.respond(embed=vote_embed)

    @discord.slash_command(name="random", description="Отправляет случайное число от a до b")
    async def random(self, ctx: ApplicationContext, a: int, b: int):
        await ctx.respond(randint(a, b))
