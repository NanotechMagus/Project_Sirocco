#!/usr/bin/python3.7

# Standard Library Imports
import requests
import json
from urllib.parse import urljoin
import time

# Locally Developed Imports
from core.core import fileHandler

# Third Party Imports

# Initial variables


class xiv:

    def __init__(self):
        self.__buildconf = fileHandler("conf", "config.json").get_data("XIVAPI")
        self.__apikey = self.__buildconf['key'] if self.__buildconf['key'] is not "" else None
        self.__api = self.__buildconf['api']
        self.__chardat = {
            "name": "",
            "server": "",
            "userid": "",
            "raw": {}
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
                            self.__chardat["name"] = name
                            self.__chardat["server"] = charname["Server"]
                            self.__chardat["userid"] = charname["ID"]
                            return True
                else:
                    return False

        except requests.exceptions.RequestException as err:
            print(f'{err} has occured')
            return False

    def xiv_get_data(self):

        if self.__chardat["userid"] is not "":

            params = {"data": "AC,FC,PVP", "private_key": self.__apikey}

            try:
                charinfo = requests.get(urljoin(self.__api, "character/" + str(self.__chardat["userid"])),
                                        params=params)

                self.__chardat["raw"] = json.loads(charinfo.content)
                return self.__chardat

            except requests.exceptions.RequestException as err:
                print(f'{err}')
                return False
        else:
            return 3


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