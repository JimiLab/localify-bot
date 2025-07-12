import logging
from discord.ext import commands
from discord import Intents, Object
import discord
from config import ARTIST_CITY_CHANNEL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LocalifyBot(commands.Bot):

    def __init__(self, application_id, guild_id):
        intents = Intents.default()
        super().__init__(command_prefix="!", intents=intents, application_id=application_id)
        self.guild_id = guild_id

    async def setup_hook(self):
        # register commands to a single guild for instant availability during dev
        guild = Object(id=self.guild_id) if self.guild_id else None
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

    async def send_embed(self,
                         title: str,
                         desc: str,
                         image: str
                         ):
        embed = discord.Embed(
            title=title,
            description=desc,
            color=discord.Color.pink()
        )
        embed.set_image(url=image)
        embed.set_author(name="Localify Dashboard", url="https://dash.localify.org/#/crowd-sourcing/artist/city")

        channel = self.get_channel(int(ARTIST_CITY_CHANNEL))
        await channel.send("", embed=embed)
