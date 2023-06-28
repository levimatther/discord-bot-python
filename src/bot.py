import os
import random

import discord

from utilities import constants, google_search, storage_service

TOKEN = os.getenv("BOT_TOKEN")


class Client(discord.Client):
    async def on_message(self, message):
        # If message is from bot itself, return #
        if self.user == message.author:
            return

        message_content = message.content

        # Send Hello message on greeting from user #
        if message_content.lower() in constants.USER_GREETING_MESSAGES:
            await message.channel.send(
                f"{random.choice(constants.BOT_GREETING_MESSAGES)} {message.author.display_name}"
            )

        # Search on Google if Message StartsWith "!google" #
        elif message_content.startswith("!google"):
            search_term = " ".join(
                message_content.split()[1:]
            )  # Gets search term from `!google leo messi` to `leo messi`#
            if not search_term:
                await message.channel.send(
                    random.choice(constants.NO_TERM_ENTERED_MESSAGES)
                )
                return

            search_service = google_search.GoogleSearch()
            results = search_service.get_top_five_links(search_term)

            embeded_response = discord.Embed(
                title=f"{constants.EMBEDDED_RESULTS_TITLE} '{search_term}'",
            )
            for result in results:
                embeded_response.add_field(
                    name=result["title"], value=result["url"], inline=False
                )
            # Persist message into db #
            storage_service.SearchHistoryService().insert_search_history(
                message.author.id, search_term
            )
            await message.channel.send(embed=embeded_response)

        # Return recent searches if message startswith "!recent" #
        elif message_content.startswith("!recent"):
            search_term = " ".join(
                message_content.split()[1:]
            )  # Gets search term from `!google leo messi` to `leo messi`#
            if not search_term:
                await message.channel.send(
                    random.choice(constants.NO_TERM_ENTERED_MESSAGES)
                )
                return
            records = (
                storage_service.SearchHistoryService().get_recent_related_searches(
                    message.author.id, search_term
                )
            )
            embedded_response = discord.Embed(
                title=f"{constants.RECENT_SEARCHES_TITLE} '{search_term}'"
            )
            for record in records:
                embedded_response.add_field(
                    name=record.search_term,
                    value=f"Searched on {record.timestamp}",
                    inline=False,
                )
            await message.channel.send(embed=embedded_response)


client = Client()
client.run(TOKEN)
