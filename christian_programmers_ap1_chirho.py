#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son,
# that all who believe in Him should not perish but have everlasting life
from typing import Optional

import aiosqlite
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
    questions_chirho = [
        "Are you: A. Protestant B. Catholic C. Orthodox D. Non-Christian",
        "Please summarize your Christian views.",
        "Why did you join this server?",
        "How old are you?",
        "Have you read the rules?",
        "Just to be sure you read the rules.. What will we do if a prosperity gospel \"teaching\" gets posted?",
        "What is your preferred programming language(s)?",
        "What is your programming experience? Rest assured, we don't base our admissions on programming experience."]

    def __init__(self):
        self.token_chirho = os.getenv("TOKEN_CHIRHO")
        self.admin_user_id_chirho = int(os.getenv("ADMIN_USER_ID_CHIRHO"))
        self.sqlite_filename_chirho = os.getenv("SQLITE_FILENAME_CHIRHO", "christian_programmers_ap1_chirho.sqlite3")
        self.join_view_channel_chirho = os.getenv("JOIN_VIEW_CHANNEL_CHIRHO", "general")
        self.db_connection_chirho: Optional[aiosqlite.core] = None
        self.bot_chirho: Optional[commands.Bot] = None
        self.admin_user_chirho: Optional[discord.User] = None
        self._setup_bot_chirho()

    async def _setup_tables_chirho(self):
        await self.db_connection_chirho.execute("""
            CREATE TABLE IF NOT EXISTS user_dms_chirho (
                user_id_chirho INTEGER PRIMARY KEY,
                content_chirho TEXT);
        """)

    async def detect_and_block_user_chirho(self, user_chirho: discord.User):
        """
        Hallelujah, if the user posts too many DMs, we will block them.
        """
        # todo: finish God willing
        pass

    async def get_user_question_text_index_chirho(self, user_chirho: discord.User) -> int:
        """
        Hallelujah, get the index of the question we should ask the user.
        :param user_chirho:
        :return:
        """
        return 0

    async def send_question_chirho(self, user_chirho: discord.User):
        question_index_chirho = await self.get_user_question_text_index_chirho(user_chirho)
        question_text_chirho = self.questions_chirho[question_index_chirho]
        await user_chirho.send(question_text_chirho)

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
            self.admin_user_chirho = self.bot_chirho.get_user(self.admin_user_id_chirho)
            self.db_connection_chirho = await aiosqlite.connect(self.sqlite_filename_chirho)
            await self._setup_tables_chirho()

            str_chirho = 'Aleluya, We have logged in as {0.user}'.format(self.bot_chirho)
            logger_chirho.info(str_chirho)
            await self.admin_user_chirho.send(str_chirho)

        @self.bot_chirho.command()
        async def apply(ctx_chirho: commands.Context):
            # Hallelujah, for testing purposes
            if ctx_chirho.author == self.bot_chirho.user:
                return

            await ctx_chirho.channel.send(
                "Thank you for joining, please apply to the Christian Programmers server.",
                view=JoinEmbedViewChirho(bot_chirho=self))

        @self.bot_chirho.event
        async def on_member_join(member_chirho: discord.User):
            logger_chirho.info(f"on_member_join {member_chirho}")
            channel_chirho = self.bot_chirho.get_channel(self.join_view_channel_chirho)
            await channel_chirho.send(
                f"Welcome {member_chirho.name} to Christian Programmers! Please apply to the server.",
                view=JoinEmbedViewChirho(bot_chirho=self))

        @self.bot_chirho.event
        async def on_message(message_chirho: discord.Message):
            if message_chirho.author == self.bot_chirho.user:
                return

            if message_chirho.channel.type == discord.ChannelType.private:
                logger_chirho.info(f"on_message {message_chirho}")
                await self.detect_and_block_user_chirho(message_chirho.author)
                await self.send_question_chirho(message_chirho.author)

            else:
                # For testing purposes, hallelujah
                await self.bot_chirho.process_commands(message_chirho)

    def run_bot_chirho(self):
        self.bot_chirho.run(self.token_chirho)


class JoinEmbedViewChirho(discord.ui.View):
    def __init__(self, *args_chirho, bot_chirho: ChristianProgrammersAp1BotChirho,  **kwargs_chirho):
        super().__init__(*args_chirho, **kwargs_chirho)
        self.bot_chirho = bot_chirho

    @discord.ui.button(label='Join', style=discord.ButtonStyle.green)
    async def join_chirho(
            self, interaction_chirho: discord.Interaction, button_chirho: discord.ui.Button, ):
        # This is called once the button is clicked
        logger_chirho.info(f"Join button clicked by {interaction_chirho } {dir(interaction_chirho)}")
        interaction_chirho.user.send("Thanks for applying to Christian Programmers!")
        await self.bot_chirho.send_question_chirho(interaction_chirho.user)
        await interaction_chirho.message.delete()


def main_chirho():
    bot_chirho = ChristianProgrammersAp1BotChirho()
    bot_chirho.run_bot_chirho()


if __name__ == '__main__':
    main_chirho()
