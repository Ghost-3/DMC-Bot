import discord
from discord.ui import Modal, View, InputText, Button, Item
from discord import Embed, Interaction, InputTextStyle


class RequestModal(Modal):
    def __init__(
            self, title: str = "Заявка",
            ephemeral_msg_text: str = "Заявка успешно отправлена",
            request_channel_id: int = 784984599435804672,
            up_emoji: str = "<:up_:1088899600997417071>",
            down_emoji: str = "<:down:1088899619632730184>",
            *args, **kwargs) -> None:
        super().__init__(title=title, *args, **kwargs)

        # Config
        self.ephemeral_msg_text = ephemeral_msg_text
        self.request_channel_id = request_channel_id
        self.up_emoji = up_emoji
        self.down_emoji = down_emoji

        self.add_item(InputText(label="Ваш ник в Minecraft", placeholder="Введите ник в Minecraft"))
        self.add_item(InputText(label="Сколько вам лет?", placeholder="Введите ваш возраст"))
        self.add_item(InputText(label="Чем вы будете заниматься на сервере?", style=InputTextStyle.long))

    async def callback(self, interaction: Interaction):
        embed = Embed(title="Заявка", color=0xb5b5b5)
        embed.add_field(name="Ник", value=self.children[0].value)
        embed.add_field(name="Возраст", value=self.children[1].value)
        embed.add_field(name="Планы на сервер", value=self.children[2].value, inline=False)
        embed.set_author(name=interaction.user.name)
        embed.set_thumbnail(url=interaction.user.avatar)

        await interaction.response.send_message(content=self.ephemeral_msg_text, ephemeral=True)
        channel = interaction.guild.get_channel(self.request_channel_id)
        msg = await channel.send(embed=embed)
        await msg.add_reaction(self.up_emoji)
        await msg.add_reaction(self.down_emoji)


class RequestView(View):
    def __init__(self, *items: Item):
        super().__init__(*items, disable_on_timeout=True)

    @discord.ui.button(label="Отправить заявку", style=discord.ButtonStyle.blurple)
    async def button_callback(self, button: Button, interaction: Interaction):
        await interaction.response.send_modal(RequestModal(title="Заявка"))
