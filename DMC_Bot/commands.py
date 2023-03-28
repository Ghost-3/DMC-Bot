from random import randint

import discord
from discord import Embed, ApplicationContext
from discord.ext import commands

from cfg import CONFIG

from utils.cravatar import Cravatar
from utils.server_status import ServerStatus
from utils.ban_list import BanList

from UI.request_modal import RequestModal, RequestView


class Commands(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self.cravatar = Cravatar()
        self.server_status = ServerStatus()
        self.ban_list = BanList()

    @discord.slash_command(name="ping", description="ping бота")
    async def ping(self, ctx: ApplicationContext):
        await ctx.respond('Pong! {0}ms'.format(round(self.bot.latency * 1000)))

    @discord.slash_command(name="help", description="Отправляет список команд")
    async def help(self, ctx: ApplicationContext):
        help_embed = Embed(
            color=0x11FF11,
            title="Help",
            description="`/ping` - Пинг бота\n"
                        "`/info` - Информация о сервере\n"
                        "`/random` - Случайное число от a до b\n"
                        "`/mc-avatar` - Плоская голова игрока\n"
                        "`/mc-head` - Голова игрока\n"
                        "`/server-status` - Статус сервера\n"
                        "`/ban-list` - Список забаненых игроков (WIP)\n"
                        "`/send-request` - Отправить заявку на проходку")
        await ctx.respond(embed=help_embed)

    @discord.slash_command(name="info", description="Отправляет информацию о сервере")
    async def info(self, ctx: ApplicationContext):
        info_embed = Embed(
            color=0x11FF11,
            title="Информация"
        )
        info_embed.add_field(name="IP сервера", value=":flag_ru: dreammc.su\n"
                                                      ":flag_ua: test.dreammc.su", inline=True)
        info_embed.add_field(name="Контакты", value="Сайт: https://dreammc.su/\n"
                                                    "ВКонтакте: https://vk.dreammc.su/\n"
                                                    "Discord: https://discord.dreammc.su/", inline=True)
        info_embed.add_field(name="Карта", value="Мир построек:\nhttps://build.dreammc.su\n"
                                                 "Мир ферм:\nhttps://farm.dreammc.su", inline=True)
        info_embed.add_field(name="Голосовать", value="https://minecraftrating.ru/vote/83916/", inline=True)
        await ctx.respond(embed=info_embed)

    @discord.slash_command(name="random", description="Отправляет случайное число от a до b")
    async def random(self, ctx: ApplicationContext, a: int, b: int):
        await ctx.respond(randint(a, b))

    @discord.slash_command(name="mc-avatar", description="Отправляет плоскую картинку головы")
    async def mc_avatar(self, ctx: ApplicationContext, nickname: str):
        embed = Embed(color=0x11FF11, title=nickname)
        embed.set_image(url=self.cravatar.helm_avatar(nickname))
        await ctx.respond(embed=embed)

    @discord.slash_command(name="mc-head", description="Отправляет объёмную картинку головы")
    async def mc_head(self, ctx: ApplicationContext, nickname: str):
        embed = Embed(color=0x11FF11, title=nickname)
        embed.set_image(url=self.cravatar.helm_head(nickname))
        await ctx.respond(embed=embed)

    @discord.slash_command(name="server-status", description="Отправляет статус сервера")
    async def server_status(self, ctx: ApplicationContext):
        status = self.server_status.get_status()

        description = "".join([char["text"] for char in status.raw['description']['extra']])

        embed = Embed(color=0x11FF11, title="DreamMC", description=description)
        embed.add_field(name="Status", value=":white_check_mark: Online" if status else ":x: Offline")
        embed.add_field(name="Players",
                        value="{}/{}".format(status.players.online, status.players.max) if status else "0/0")
        embed.set_image(url=ServerStatus.favicon_url)
        await ctx.respond(embed=embed)

    @discord.slash_command(name="ban-list", description="Отправляет список забаненых пользователей")
    async def ban_list(self, ctx: ApplicationContext, page: int):
        data = self.ban_list.get_page(page)
        ban_list = "\n".join(" | ".join(
            (str(pl.order), pl.name, pl.source, pl.created.isoformat(), pl.reason)) for pl in data)
        embed = Embed(color=0x11FF11,
                      title="BanList",
                      description="**Page {page}**\n{ban_list}".format(page=page, ban_list=ban_list))
        await ctx.respond(embed=embed)

    @discord.slash_command(name="send-request", description="Открывает окно заполнения заявки")
    async def send_request(self, ctx: ApplicationContext, button: bool = False):
        if button:
            await ctx.respond(view=RequestView())
        else:
            await ctx.send_modal(RequestModal("Заявка", **CONFIG["request"]["modal"]))

