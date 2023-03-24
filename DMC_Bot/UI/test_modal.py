import discord
from discord.ui import Modal, View, InputText, Button, Item
from discord import Embed, Interaction, InputTextStyle, ApplicationContext


class MyModal(Modal):
    def __init__(self, title: str = "Модальное окно", *args, **kwargs) -> None:
        super().__init__(title=title, *args, **kwargs)

        self.add_item(InputText(label="Введите ник"))
        self.add_item(InputText(label="Введите текст", style=InputTextStyle.long))

    async def callback(self, interaction: Interaction):
        embed = Embed(title="Результат")
        embed.add_field(name="Ник", value=self.children[0].value)
        embed.add_field(name="Текст", value=self.children[1].value)
        await interaction.response.send_message(embeds=[embed])


class MyView(View):
    def __init__(self, ctx: ApplicationContext, *items: Item):
        super().__init__(*items)
        self.ctx = ctx

    async def interaction_check(self, interaction: Interaction):
        if int(interaction.user.id) == int(self.ctx.user.id):
            return True
        else:
            await interaction.response.send_message("Это сообщение предназначено для другого.", ephemeral=True)
            return False

    @discord.ui.button(label="Вызвать модальное окно")
    async def button_callback(self, button: Button, interaction: Interaction):
        await interaction.response.send_modal(MyModal(title="Модальное окно"))
        await interaction.delete_original_response()
