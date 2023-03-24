import discord
from discord.ui import Modal, View, InputText, Button, Item
from discord import Embed, Interaction, InputTextStyle, ApplicationContext, Emoji


class RequestModal(Modal):
    def __init__(self, title: str = "Заявка", *args, **kwargs) -> None:
        super().__init__(title=title, *args, **kwargs)

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

        await interaction.response.send_message(embeds=[embed])
        msg: discord.InteractionMessage = await interaction.original_response()
        await msg.add_reaction("<:up_:1088899600997417071>")
        await msg.add_reaction("<:down:1088899619632730184>")


class RequestView(View):
    def __init__(self, *items: Item):
        super().__init__(*items)

    @discord.ui.button(label="Отправить заявку")
    async def button_callback(self, button: Button, interaction: Interaction):
        await interaction.response.send_modal(RequestModal(title="Заявка"))
