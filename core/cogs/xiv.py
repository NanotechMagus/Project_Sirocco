#!/usr/bin/python

# Standard Library Imports
import random
import string
import json

# Third Party Imports
import discord
from discord.ext import commands

# Locally Developed Imports
from core.games import xiv as sxiv
from core.discord import EmbedMe


class xiv(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(
        name="Character Search",
        aliases=[
            'character',
            'char',
            'Char'
        ],
        description="Search the lodestone for a character!"
    )
    async def character_info(
            self,
            ctx,
            fname: str,
            lname: str,
            server='Balmung'
    ):

        cid = sxiv()

        try:
            if cid.xiv_get_id(f'{fname} {lname}', server):

                embedded = EmbedMe().embed_builder(cid.xiv_get_char_data(), "xiv_char")

                embed = discord.Embed(
                    title=embedded['title'],
                    url=embedded['url'],
                    description=embedded['description']
                )

                embed.set_image(url=embedded['image']['url'])
                embed.set_footer(text=embedded['footer']['text'])

                for fields in embedded['fields']:
                    embed.add_field(
                        name=fields['name'],
                        value=fields['value'],
                        inline=fields['inline']
                    )

                await ctx.send(embed=embed)
            else:
                await ctx.send(f'I could not find {fname} {lname} on {server}.  Please try again.')
                return

        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    @commands.command(
        name="Bad RP Profiles",
        aliases=["brp"],
        description="Spin the wheel and see what's inside!"
    )
    async def brp(self, ctx):

        brpadditive = random.sample(sxiv.brp(), 6)

        await ctx.send(f"```{brpadditive[0]}  {brpadditive[1]} "
                       f"\n{brpadditive[2]}  {brpadditive[3]}"
                       f"\n{brpadditive[4]}  {brpadditive[5]}```")


def setup(client):
    client.add_cog(xiv(client))
