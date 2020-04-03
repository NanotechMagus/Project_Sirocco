#!/usr/bin/python3.8

# Standard Library Imports
import datetime

# Third Party Imports
import discord
from discord.ext import commands, tasks

# Locally Developed Imports
from core.google import gcal


class disCal(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.banannounce = []
        self.calendar = gcal()
        self.tomorrow.start()

    @commands.command(
        name='birthday',
        description='Who\'s birthday is next?',
        alias='nextbirthday'
    )
    async def birthday(self, ctx, results=1):
        bdict = self.calendar.get_cal(results)

        if bdict:

            await ctx.send(f"The next birthday{'s' if len(bdict) != 1 else ''} "
                           f"{'are' if bdict != 1 else 'is'}:\n"
                           f"```{','.join(str(bdict)).splitlines()}```")

        return

    @commands.command(
        name='birthday announcement list',
        alias='bdayannounce'
    )
    async def bdayannounce(self, ctx):
        member = ctx.author
        if not member.id in self.banannounce:
            self.banannounce.append(member)
            await ctx.send(f"{member.name} have been added to the list!")

    def cog_unload(self):
        self.tomorrow.cancel()

    @tasks.loop(hours=24)
    async def tomorrow(self, ctx):
        blist = self.calendar.get_cal(1)
        today = datetime.date.today()
        tomorrow = today.replace(day=today.day + 1)
        birthday = datetime.datetime.strptime(blist[0][:10], "%Y-%m-%d")
        name = blist[0][11:]

        if birthday.date() == tomorrow:
            for x in self.banannounce:
                await x.send(f"{name} is tomorrow!")

        discord.ext.tasks.Loop.next_iteration(datetime.time(hour=19))


def setup(client):
    client.add_cog(disCal(client))