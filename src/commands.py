from discord import Interaction
from discord import app_commands
from bot import LocalifyBot, logger
from config import GUILD_ID, APPLICATION_ID

bot = LocalifyBot(APPLICATION_ID, GUILD_ID)


@bot.tree.command(name="register", description="Register a message")
@app_commands.describe(msg="Your registration message")
async def register(interaction: Interaction, msg: str):
    logger.info(f"[REGISTER] {interaction.user} → {msg}")
    await interaction.response.send_message("✅ Registered your message!", ephemeral=True)
