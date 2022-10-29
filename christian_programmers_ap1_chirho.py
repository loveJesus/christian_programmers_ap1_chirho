#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son,
# that all who believe in Him should not perish but have everlasting life
from typing import Optional

import discord
import dotenv
import logging
import os
import sys

from discord.ext import commands
from icecream import ic

dotenv.load_dotenv()

logging.basicConfig(stream=sys.stderr, encoding='utf-8', level=logging.INFO)
logger_chirho = logging.getLogger(__file__)


class ChristianProgrammersAp1BotChirho:
    def __init__(self):
        self.token_chirho = os.getenv("TOKEN_CHIRHO")
        self.admin_user_id_chirho = int(os.getenv("TOKEN_ADMIN_USER_ID_CHIRHO"))
        self.bot_chirho: Optional[commands.Bot] = None
        self._setup_bot_chirho()

    def _setup_bot_chirho(self):
        description_chirho = """
        A bot that logs answers to the new member form for the Christian Programmers discord server.
        """
        intents_chirho = discord.Intents.default()
        intents_chirho.message_content = True
        intents_chirho.members = True
        self.bot_chirho = commands.Bot(command_prefix="?", description=description_chirho, intents=intents_chirho)

        @self.bot_chirho.event
        async def on_ready():
            user_chirho = self.bot_chirho.get_user(self.admin_user_id_chirho)
            str_chirho = 'Aleluya, We have logged in as {0.user}'.format(self.bot_chirho)
            logger_chirho.info(str_chirho)
            await user_chirho.send(str_chirho)

        @self.bot_chirho.command()
        async def apply(ctx_chirho: commands.Context):
            if ctx_chirho.author == self.bot_chirho.user:
                return

            await ctx_chirho.author.send("Jesus Christ is Lord")

            print(ctx_chirho.channel.name + ctx_chirho.message.content)

            if 'aleluya' in ctx_chirho.message.content:
                await ctx_chirho.channel.send('Hallelujah!')

    def run_bot_chirho(self):
        self.bot_chirho.run(self.token_chirho)


def main_chirho():
    bot_chirho = ChristianProgrammersAp1BotChirho()
    bot_chirho.run_bot_chirho()


if __name__ == '__main__':
    main_chirho()
