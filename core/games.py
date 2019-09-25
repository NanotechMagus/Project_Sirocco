#!/usr/bin/python3.7

# Standard Library Imports
import requests
import json
from urllib.parse import urljoin

# Locally Developed Imports
from core.core import fileHandler

# Third Party Imports

# Initial variables


class xiv:

    def __init__(self):
        buildconf = fileHandler("conf", "XIVAPI")

        self.__api = buildconf['api']
        self.__apikey = buildconf['key']
        self.chardat = {
            "name": "",
            "server": "",
            "userid": "",
            "raw": {}
        }


class div2:

    def __init__(self):
        buildconf = fileHandler("conf", "XIVAPI")

        self.__api = buildconf['api']
        self.__apikey = buildconf['key']
        self.chardat = {
            "name": "",
            "server": "",
            "userid": "",
            "raw": {}
        }