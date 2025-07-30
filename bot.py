import discord
from discord.ext import commands
import os
from models import get_image_description

TOKEN = os.getenv("DISCORD_TOKEN")  # Colocar o token do bot nas variáveis de ambiente no Render

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Para ler mensagens e anexos

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

# Comando para descrever imagens
@bot.command()
async def descrever(ctx):
    if not ctx.message.attachments:
        await ctx.send("Envie uma imagem junto com o comando, Felipe!")
        return

    # Pega a primeira imagem enviada
    image = ctx.message.attachments[0]
    await image.save("temp.jpg")

    # Chama a IA para descrever
    descricao = get_image_description("temp.jpg")
    await ctx.send(f"Descrição: {descricao}")

bot.run(TOKEN)
