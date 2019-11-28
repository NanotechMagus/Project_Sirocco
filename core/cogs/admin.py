#!/usr/bin/python

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
from core.core import fileHandler


class admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    # TODO: Not working with discord.py v1.2.5, but will work with 1.3.0 once out of alpha (uses new methods)
    '''
    @commands.command(
        name="Initialize the Guild Datastore",
        hidden=True,
        aliases=[
            "init"
        ]
    )
    @commands.has_permissions(administrator=True)
    async def init_guild(self, ctx):
        fh = fileHandler("core\\data", "member.dat")
        # datastore = fh.get_data()
        try:
            members = await discord.guild.fetch_members(limit=150).flatten()
            for users, userid in enumerate(members):
                datastore[users] = {"dstats": {}, "gamedata": {}}
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

        # with open(fh.datfile, "w") as f:
        #    json.dumps(datastore, f)
    '''


def setup(client):
    client.add_cog(admin(client))
