import discord
from discord.ext import commands

# ID del ruolo
ROLE_ID = 1506565867696164934

# parola da controllare nello status
TARGET_TEXT = "/rlchh"

intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Loggato come {bot.user}")

@bot.event
async def on_presence_update(before, after):

    role = after.guild.get_role(ROLE_ID)
    if not role:
        return

    custom_status = None

    for activity in after.activities:
        if isinstance(activity, discord.CustomActivity):
            custom_status = activity.name
            break

    status_text = (custom_status or "").lower()

    try:
        if TARGET_TEXT.lower() in status_text:

            if role not in after.roles:
                await after.add_roles(role)
                print(f"Ruolo aggiunto a {after}")

        else:

            if role in after.roles:
                await after.remove_roles(role)
                print(f"Ruolo rimosso da {after}")

    except Exception as e:
        print(e)

# 👇 metti il tuo token qui
TOKEN = os.getenv("DISCORD_TOKEN")

bot.run(TOKEN)