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
        self.join_view_channel_id_chirho = int(os.getenv("JOIN_VIEW_CHANNEL_ID_CHIRHO", "general"))
        self.db_connection_chirho: Optional[aiosqlite.core] = None
        self.bot_chirho: Optional[commands.Bot] = None
        self.admin_user_chirho: Optional[discord.User] = None
        self._setup_bot_chirho()

    async def _setup_tables_chirho(self):
        await self.db_connection_chirho.execute("""
            CREATE TABLE IF NOT EXISTS user_dms_chirho (
                pk_chirho INTEGER PRIMARY KEY AUTOINCREMENT,
                date_time_chirho DATETIME DEFAULT CURRENT_TIMESTAMP,
                is_reset_chirho BOOLEAN DEFAULT 0,
                question_index_chirho INTEGER DEFAULT NULL,       
                user_id_chirho INTEGER NOT NULL,
                user_name_chirho TEXT NOT NULL,
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
        cursor_chirho = await self.db_connection_chirho.execute("""
            SELECT is_reset_chirho, question_index_chirho from user_dms_chirho WHERE user_id_chirho = ? ORDER BY pk_chirho DESC LIMIT 1;
        """, (user_chirho.id,))
        row_chirho = await cursor_chirho.fetchone()
        await cursor_chirho.close()

        if row_chirho is None:
            logger_chirho.exception(f"User {user_chirho} has no questions in the database.")
            return 0
        if row_chirho[0]:
            return 0
        return row_chirho[1] + 1

    async def send_admin_user_response_chirho(self, user_chirho: discord.User):
        """
        Hallelujah, send the admin a report of a complete user a response.
        :param user_chirho:
        :return:
        """
        logger_chirho.info(f"Sending admin user response for {user_chirho}")
        await self.admin_user_chirho.send(f"{user_chirho.name} has finished the application process.")
        cursor_chirho = await self.db_connection_chirho.execute("""
            SELECT pk_chirho from user_dms_chirho WHERE user_id_chirho = ? AND is_reset_chirho = 1 ORDER BY pk_chirho DESC LIMIT 1;
        """, (user_chirho.id,))
        row_chirho = await cursor_chirho.fetchone()
        await cursor_chirho.close()
        if not row_chirho:
            begin_pk_chirho = 0
        else:
            begin_pk_chirho = row_chirho[0]
        logger_chirho.info(f"User {user_chirho} minPK_chirho {begin_pk_chirho}.")
        cursor_chirho = await self.db_connection_chirho.execute("""
            SELECT question_index_chirho, content_chirho from user_dms_chirho WHERE user_id_chirho = ? AND pk_chirho > ? AND question_index_chirho < ? ORDER BY pk_chirho;
        """, (user_chirho.id, begin_pk_chirho, len(self.questions_chirho)))
        responses_chirho = []
        async for row_chirho in cursor_chirho:
            logger_chirho.info(f"Sending admin user response for {user_chirho} question id {row_chirho[0]} answer {row_chirho[1]}")
            responses_chirho.append(f"{user_chirho.name}: {self.questions_chirho[row_chirho[0]]}\n{row_chirho[1]}")
        await cursor_chirho.close()
        await self.admin_user_chirho.send("\n".join(responses_chirho))


    async def send_response_chirho(self, user_chirho: discord.User):
        question_index_chirho = await self.get_user_question_text_index_chirho(user_chirho)
        if question_index_chirho >= len(self.questions_chirho):
            logger_chirho.info(f"User {user_chirho} has finished the application process, current question index = {question_index_chirho}.")
            if question_index_chirho == len(self.questions_chirho):
                await self.send_admin_user_response_chirho(user_chirho)

            await user_chirho.send("Thank you for your application. We will review it soon, God bless in Jesus' name.")
            return
        question_text_chirho = self.questions_chirho[question_index_chirho]
        await user_chirho.send(question_text_chirho)

    async def store_user_dm_chirho(self, message_chirho: discord.Message):
        """
        Hallelujah, store the user's DM in the database.
        :param message_chirho:
        :return:
        """
        question_index_chirho = await self.get_user_question_text_index_chirho(message_chirho.author)
        await self.db_connection_chirho.execute("""
            INSERT INTO user_dms_chirho (question_index_chirho, user_id_chirho, user_name_chirho, content_chirho)
            VALUES (?, ?, ?, ?);
        """, (question_index_chirho, message_chirho.author.id, message_chirho.author.name, message_chirho.content))
        await self.db_connection_chirho.commit()

    async def new_user_application_chirho(self, user_chirho: discord.User):
        """
        Start a new user application.
        :param user_chirho:
        :return:
        """
        await user_chirho.send(
            "Thanks for applying to Christian Programmers! Please answer the following questions. "
            "I am sorry we currently only read your answers without edits. "
            "If you make a mistake you can type `?apply` to start from the beginning again.")
        await self.db_connection_chirho.execute("""
            INSERT INTO user_dms_chirho (is_reset_chirho, user_id_chirho, user_name_chirho)
            VALUES (?, ?, ?);
        """, (1, user_chirho.id, user_chirho.name))
        await self.db_connection_chirho.commit()
        await self.send_response_chirho(user_chirho)

    def _setup_bot_chirho(self):
        bot_char_chirho = "?"
        description_chirho = """
        A bot that logs answers to the new member form for the Christian Programmers discord server.
        """
        intents_chirho = discord.Intents.default()
        intents_chirho.message_content = True
        intents_chirho.members = True
        self.bot_chirho = discord.Client(description=description_chirho, intents=intents_chirho)

        @self.bot_chirho.event
        async def on_ready():
            self.admin_user_chirho = self.bot_chirho.get_user(self.admin_user_id_chirho)
            self.db_connection_chirho = await aiosqlite.connect(self.sqlite_filename_chirho)
            await self._setup_tables_chirho()

            str_chirho = 'Aleluya, We have logged in as {0.user}'.format(self.bot_chirho)
            logger_chirho.info(str_chirho)
            await self.admin_user_chirho.send(str_chirho)

        async def apply(message_chirho: discord.Message):
            if message_chirho.author == self.bot_chirho.user:
                return

            logger_chirho.info("User %s has started a new application.", message_chirho.author)

            await message_chirho.channel.send(
                f"Thank you {message_chirho.author.name} for joining, please apply to the Christian Programmers server.",
                view=JoinEmbedViewChirho(cp_bot_chirho=self))

        @self.bot_chirho.event
        async def on_member_join(member_chirho: discord.User):
            logger_chirho.info(f"on_member_join {member_chirho} notify {self.join_view_channel_id_chirho}")
            channel_chirho = self.bot_chirho.get_channel(self.join_view_channel_id_chirho)
            await channel_chirho.send(
                f"Welcome {member_chirho.name} to Christian Programmers! Please apply to the server.",
                view=JoinEmbedViewChirho(cp_bot_chirho=self))

        @self.bot_chirho.event
        async def on_message(message_chirho: discord.Message):
            if message_chirho.author == self.bot_chirho.user:
                return

            if not message_chirho.content.startswith(bot_char_chirho) and message_chirho.channel.type == discord.ChannelType.private:
                logger_chirho.info(f"on_message {message_chirho}")
                await self.detect_and_block_user_chirho(message_chirho.author)
                await self.store_user_dm_chirho(message_chirho)
                await self.send_response_chirho(message_chirho.author)

            elif message_chirho.content.startswith(bot_char_chirho+"apply"):
                await apply(message_chirho)

            elif message_chirho.content.startswith(bot_char_chirho+"test_chirho"):
                logger_chirho.info("Sending info to " + str(self.join_view_channel_id_chirho))
                channel_chirho = self.bot_chirho.get_channel(self.join_view_channel_id_chirho)
                await channel_chirho.send("Hallelujah, this is a test message from the bot.")

    def run_bot_chirho(self):
        self.bot_chirho.run(self.token_chirho)


class JoinEmbedViewChirho(discord.ui.View):
    def __init__(self, *args_chirho, cp_bot_chirho: ChristianProgrammersAp1BotChirho,  **kwargs_chirho):
        super().__init__(*args_chirho, **kwargs_chirho)
        self.cp_bot_chirho = cp_bot_chirho

    @discord.ui.button(label='Join', style=discord.ButtonStyle.green)
    async def join_chirho(
            self, interaction_chirho: discord.Interaction, button_chirho: discord.ui.Button, ):
        # This is called once the button is clicked
        logger_chirho.info(f"Join button clicked by {interaction_chirho } {dir(interaction_chirho)}")
        await self.cp_bot_chirho.new_user_application_chirho(interaction_chirho.user)
        await interaction_chirho.message.delete()


def main_chirho():
    bot_chirho = ChristianProgrammersAp1BotChirho()
    bot_chirho.run_bot_chirho()


if __name__ == '__main__':
    main_chirho()
