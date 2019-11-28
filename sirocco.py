#!/usr/bin/python3.7

# Standard Library Imports
import logging
import os

# Locally Developed Imports
from core.core import initialize

# Third Party Imports
from discord.ext import commands

log = logging.basicConfig()


def main():

    init = initialize()

    sirocco = commands.Bot(command_prefix=init.disconf['PREFIX'], description=init.disconf['DESCRIPTION'])

    for extension in gather_extensions(init.cogdir):
        try:
            print(f'{extension}')
            sirocco.load_extension(extension)
        except FileNotFoundError as err:
            logging.warning(f'Failed to load extension {extension}.')

    sirocco.run(init.disconf['TOKEN'], bot=True, restart=True)

    return


def gather_extensions(basedir):

    cogsdir = os.path.join(basedir, "cogs")
    reglist = [f for f in os.listdir(cogsdir) if os.path.isfile(os.path.join(cogsdir, f))]
    splitlist = [os.path.splitext(x)[0] for x in reglist]

    return ["core.cogs." + x for x in splitlist]


if __name__ == "__main__":
    main()

