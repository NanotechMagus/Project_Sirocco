#!/usr/bin/python3.7

# Standard Library Imports
import logging
import os
# Locally Developed Imports

# Third Party Imports
from discord.ext import commands

# Initial variables
disconf = {}
basedir = ""


def __init__():
    from core.core import fileReader
    global basedir
    global disconf

    conffile = fileReader('conf', 'config.json')
    disconf = conffile.get_data('Disord')
    basedir = conffile.basePath


def main():

    sirocco = commands.Bot(command_prefix=disconf['PREFIX'], description=disconf['DESCRIPTION'])

    for extension in gather_extensions():
        try:
            sirocco.load_extension(extension)
        except FileNotFoundError as err:
            logging.warning(f'Failed to load extension {extension}.')

    sirocco.run(token=disconf['TOKEN'])

    return


def gather_extensions():

    cogsdir = os.path.join(basedir, "cogs")
    reglist = [f for f in os.listdir(cogsdir) if os.path.isfile(os.path.join(cogsdir, f))]
    splitlist = [os.path.splitext(x)[0] for x in reglist]

    return ["cogs." + x for x in splitlist]
