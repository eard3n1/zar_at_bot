import os
from dotenv import load_dotenv
from discord import Client, Intents, Interaction, app_commands
from response_handler import get_response

# load token from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD")

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)
tree = app_commands.CommandTree(client)

# startup
@client.event
async def on_ready():
    print(f"{client.user} is currently running")
    await tree.sync()
    print("Slash commands synced successfully")

#/ command #1
@tree.command(name="yardim", description="Yardim menusu")
async def yardim(interaction: Interaction):
    help_text = (
        "***Genel Bilgi:***\n"
        '*Zar atmak icin mesajinda "zar" & "at" kelimelerini kullanman gerekir.*\n'
        '__*Ornek:*__ *"hemen at su zari!*"\n\n'

        "***Komutlar:***\n"
        "__*/bos_yap*__ - *(1 - 100) Botun bos yapma oranini belirler*\n"
        "__*/ping*__ - *Botun gecikme durumunu gosterir*\n"
    )
    await interaction.response.send_message(
        help_text,
        ephemeral=True
    )

#/ command #2
@tree.command(name="ping", description="ping durumu")
async def ping(interaction: Interaction):
    print(f"Ping command executed, result: {round(client.latency * 1000)}ms")
    await interaction.response.send_message(
        f"gecikme: {round(client.latency * 1000)}ms",
        ephemeral=True
    )

#/ command #3
bos_yapma_orani = 10 # Default value assigned here for some reason
@tree.command(name="bos_yap", description='Bos yapma orani (1 - 100), "0" ile varsayilan deger (10)')
async def set_bos_yap(interaction: Interaction, oran: int):
    global bos_yapma_orani

    if interaction.guild is None:
        await interaction.response.send_message(
            "Bu komut ozel mesajlarda kullanilamaz.",
            ephemeral=True
        )
        return
    
    # admin prequisite (could be removed or modified as needed)
    if not interaction.user.guild_permissions.administrator: # Could also add specific user ID check here
        await interaction.response.send_message(
            "Bu komutu yalnizca yoneticiler kullanabilir.",
            ephemeral=True
        )
        return

    user = str(interaction.user)

    if 1 <= oran <= 100:
        bos_yapma_orani = oran
        print(f"bos_yap set to: ({oran}) by {user}")
        await interaction.response.send_message(f"Bos yapma orani {oran}% olarak ayarlandi")

    elif oran == 0:
        bos_yapma_orani = 10
        print(f"Bos_yap reset to default (10) by {user}")
        await interaction.response.send_message("Bos yapma olasiligi varsayilan deger olan 10% olarak ayarlandi")

    else: await interaction.response.send_message('Lutfen 1 ile 100 arasinda bir deger giriniz veya "0" ile varsayilan degeri (10) kullanin')

# message (receiving)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    server = str(message.guild)

    print(f'[{server}][{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# message (sending)
async def send_message(message, user_message):
    if not user_message:
        print("Message empty")
        return

    try:
        response = get_response(user_message, bos_yapma_orani)

        if response is None:
            print("No response generated")
            return

        print(f"Response: {response}")
        await message.channel.send(response)

    except Exception as error:
        print(f"Error out of scope: {error}")

def main():
    print("Booting up...")
    client.run(token=TOKEN)

if __name__ == "__main__":
    assert TOKEN is not None, "TOKEN was not found."
    print("TOKEN found, starting bot...")
    main()