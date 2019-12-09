#!/usr/bin/python3.7

# Standard Library Imports
import requests
import json
from urllib.parse import urljoin
import time
import random

# Locally Developed Imports
from core.core import fileHandler

# Third Party Imports

# Initial variables


class xiv:

    def __init__(self):
        self.__buildconf = fileHandler("conf", "config.json").get_data("XIVAPI")
        self.__apikey = self.__buildconf['key'] if self.__buildconf['key'] is not "" else None
        self.__api = self.__buildconf['api']
        self.chardat = {
            "name": "",
            "server": "",
            "userid": ""
        }

    def xiv_get_id(self, name: str, server: str):

        params = {"name": name.title(), "server": server.title(), "private_key": self.__apikey}

        try:

            xivid = requests.get(urljoin(self.__api, "character/search"), params=params)
            if xivid.status_code is requests.codes.ok:
                xivsearch = json.loads(xivid.content)
                if xivsearch['Pagination']['ResultsTotal'] >= 1:
                    for charname in xivsearch['Results']:
                        if charname['Name'] == name:
                            self.chardat["name"] = name
                            self.chardat["server"] = charname["Server"]
                            self.chardat["userid"] = charname["ID"]
                            return True
                else:
                    return False

        except requests.exceptions.RequestException as err:
            print(f'{err} has occured')
            return False

    def xiv_get_char_data(self):

        if self.chardat["userid"] is not "":

            params = {"data": "AC,FC,PVP", "private_key": self.__apikey}

            try:
                charinfo = requests.get(urljoin(self.__api, "character/" + str(self.chardat["userid"])),
                                        params=params)

                return json.loads(charinfo.content)

            except requests.exceptions.RequestException as err:
                print(f'{err}')
                return False
        else:
            return 3

    def get_item_data(self, item: str, info: int):
        params = {
            "columns": 'ID,Name,Icon',
            "private_key": self.__apikey
        }

        try:

            data = requests.get(urljoin(self.__api, item + "/" + str(info)), params=params)

            return json.loads(data.content)

        except requests.exceptions.RequestException as err:
            print(f'**`ERROR:`** {type(err).__name__} - {err}')
            return 0

    def brp(self):

        brpdefs = {
            "sexuality": [
                "Asexual",
                "Bi",
                "\u2640 + \u2640",
                "\u2642 + \u2642",
                "Pansexual",
                "Hetero-flexible",
                "Gay",
                "Full Lesbian",
                "Thirsty"
            ],
            "gender": [
                "Bulky Female (in male body)",
                "Delicate Male (in female body)",
                "Switch",
                "Futa",
                f"{random.choice(['Small', 'Tall'])} for age"
            ],
            "race": [
                f"Hybrid {random.choice(['Hyur', 'Roegadyn', 'Miqote', 'Lupin'])}"
                f" / {random.choice(['Viera', 'Lalafel', 'Au Ra', 'Sahagin'])}",
                "Actually a mythological creature",
                "Vampire",
                f"{random.choice(['Void', 'Light'])} touched",
                "Shapeshifter"
            ],
            "descriptors": [
                f"{random.choice(['Mhachi', 'Amdaporian', 'Nymian', 'Allagan'])}",
                "Witch",
                "Garlean Spy",
                "THE Warrior of Light",
                "Has Multiple Job Stones",
                "M/D/E/RP",
                "Lewd",
                f"{random.choice(['Prince', 'Princess'])}",
                "Clumsy",
                "Faeborn",
                "Magitech Prosthetics"
            ]
        }

        return brpdefs["sexuality"] + brpdefs["gender"] + brpdefs["race"] + brpdefs["descriptors"]



class div2:

    def __init__(self):
        self.__buildconf = fileHandler("conf", "config").get_data("Division2API")
        self.__apikey = self.__buildconf['key']
        self.__api = self.__buildconf['api']
        self.chardat = {
            "name": "",
            "server": "",
            "userid": "",
            "raw": {}
        }

    def div2_id(self, name: str, server: str):

        return

    def div2_data(self):

        return

