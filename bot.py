import discord
from discord.ext import commands
import json

with open("config.json") as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="made by reverse | v.1.0"))
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=config["GUILD_ID"]))
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="ticket", description="Open a support ticket", guild=discord.Object(id=config["GUILD_ID"]))
async def ticket(interaction: discord.Interaction):
    overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
        interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
        interaction.guild.get_role(config["SUPPORT_ROLE_ID"]): discord.PermissionOverwrite(view_channel=True)
    }

    ticket_channel = await interaction.guild.create_text_channel(
        name=f"ticket-{interaction.user.name}",
        overwrites=overwrites,
        category=interaction.guild.get_channel(config["TICKET_CATEGORY_ID"]),
        topic=f"Support ticket for {interaction.user}"
    )

    await ticket_channel.send(f"{interaction.user.mention} Thank you for opening a ticket! A support team member will assist you soon.\nType `!close` to close this ticket.")
    await interaction.response.send_message(f"🎫 Ticket created: {ticket_channel.mention}", ephemeral=True)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower() == "!close" and message.channel.name.startswith("ticket-"):
        await message.channel.send("🔒 Closing ticket in 5 seconds...")
        await discord.utils.sleep_until(discord.utils.utcnow() + discord.utils.timedelta(seconds=5))
        await message.channel.delete()

bot.run(config["TOKEN"])
