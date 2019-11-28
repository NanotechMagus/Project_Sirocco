#!/usr/bin/python3.7

# Standard Library Imports
from urllib.parse import urljoin

# Locally Developed Imports

# Third Party Imports

# Initial variables


class EmbedMe:

    def __init__(self):
        self.__embed = None
        self.__embedded = {}
        self.dataset = {
            "xiv_item": "",
            "xiv_char": self.__xiv_char,
            "xiv_glam": "",
            "div2": "",
            "bnet": ""
        }

    def embed_builder(self, edata: dict, etype: str):

        if self.dataset[etype](edata):

            return self.__embedded

    def __xiv_char(self, edata: dict):
        from core.games import xiv

        exiv = xiv()
        itertop = ["Name", "Nameday", "Portrait", "Server", "TitleTop"]
        iterbottom = ["Title", "Tribe"]
        builder = {
            "FC": edata["FreeCompany"]["Name"],
            "FCTag": edata["FreeCompany"]["Tag"],
            "ActiveClass": str(self.__name_split(edata["Character"]["ActiveClassJob"]["Name"])).title(),
            "ActiveLevel": str(edata["Character"]["ActiveClassJob"]["Level"]),
            "GrandCompany": exiv.get_item_data("GrandCompany", edata["Character"]["GrandCompany"]["NameID"])["Name"],
            "URL": f"{urljoin('https://na.finalfantasyxiv.com/lodestone/character/', str(edata['Character']['ID']))}"
        }

        for keys in edata["Character"]:
            if keys in itertop:
                builder[keys] = edata["Character"][keys]
            elif keys in iterbottom:
                builder[keys] = exiv.get_item_data(keys, edata["Character"][keys])["Name"]

        if builder["TitleTop"] is False:
            builder["NameTitle"] = f"{builder['Name']} {builder['Title']}"
        elif builder["TitleTop"]:
            builder["NameTitle"] = f"{builder['Title']} {builder['Name']}"
        else:
            builder["NameTitle"] = f"{builder['Name']}"

        if edata["AchievementsPublic"]:
            recent = [0, 0]
            for items in edata["Achievements"]["List"]:
                if items["Date"] > recent[0]:
                    recent = [items["Date"], items["ID"]]
            builder["RecentAchieve"] = exiv.get_item_data("Achievement", recent[1])["Name"]
        else:
            builder["RecentAchieve"] = "No Data Available"

        self.__embedded = {
                "title": f"{builder['NameTitle']} <{builder['FCTag']}> of {builder['Server']}",
                "description": f"**Level {builder['ActiveLevel']} {builder['Tribe']} {builder['ActiveClass']}**",
                "url": f"{builder['URL']}",
                "color": "13808143",  # Add functionality to match GC colors
                "image": {
                    "url": f"{builder['Portrait']}"
                },
                "footer": {
                    "text": f"For more information about Glamour, type ~glam {builder['Name']} {builder['Server']} (Note: Not implemented yet.)"
                },
                "fields": [
                    {
                        "name": "Free Company",
                        "value": f"{builder['FC']} - <{builder['FCTag']}>",
                        "inline": False
                    },
                    {
                        "name": "Grand Company",
                        "value": f"{builder['GrandCompany']}",
                        "inline": False
                    },
                    {
                        "name": "Nameday",
                        "value": f"{builder['Nameday']}",
                        "inline": True
                    },
                    {
                        "name": "Most Recent Achievement",
                        "value": f"{builder['RecentAchieve']}",
                        "inline": True
                    }
                ]
            }

        return True

    # Names in the API are combined as "X \/ Y".  "Y" is returned
    def __name_split(self, name: str):
        split = name.split("/")
        return split[1]

