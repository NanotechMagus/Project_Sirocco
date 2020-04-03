#!/usr/bin/python3.8

# Standard Library Imports
import random
import string
import json
from datetime import datetime as d

# Third Party Imports
import discord
from discord.ext import commands
from urllib.parse import urljoin

# Locally Developed Imports


class base(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(
        name='ping',
        description='The ping command',
        aliases=['p']
    )
    async def ping_command(self, ctx):
        start = d.timestamp(d.now())
        # Gets the timestamp when the command was used

        msg = await ctx.send(content='Pinging')
        # Sends a message to the user in the channel the message with the command was received.
        # Notifies the user that pinging has started

        await msg.edit(content=f'Pong!\nOne message round-trip took {(d.timestamp(d.now()) - start) * 1000}ms.')
        # Ping completed and round-trip duration show in ms
        # Since it takes a while to send the messages, it will calculate how much time it takes to edit an message.
        # It depends usually on your internet connection speed

        return


def setup(client):
    client.add_cog(base(client))
