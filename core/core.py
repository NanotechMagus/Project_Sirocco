#!/usr/bin/python3.7

# Standard Library Imports
import os
import json
import logging

# Locally Developed Imports

# Third Party Imports

# Initial variables


# Class for reading JSON files within the core/data directory
class fileHandler:

    # TODO: Change out init values to be more consistant -- single location
    def __init__(self, filetype: str, page: str):
        self.__basePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.datpath = os.path.join(self.__basePath, filetype)
        self.datfile = os.path.join(self.datpath, page)

    # Private wrapper
    def __validate_file(self, func):
        def cvf(*args, **kwargs):
            if os.path.exists(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                return FileNotFoundError
        return cvf

    # Get data from specific page on call, return all info under key
    # @__validate_file
    def get_data(self, keystore=None):
        try:
            data = json_open(self.datfile)
        except FileNotFoundError as err:
            errorHandler(err)
            return False
        else:
            return data if keystore is None else data[keystore]


class initialize:

    def __init__(self):
        self.__fh = fileHandler('conf', 'config.json')
        self.cogdir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "core")
        self.disconf = self.__fh.get_data('Discord')


# Basic print function designed specifically for errors
# TODO: Tie into logging function
def errorHandler(error):
    print(f'There was an error found: {error}')


# A quick and dirty function to open json files.  This function assumes that the file exists and is readable
# TODO: Harden and design for error correcting.
def json_open(filename):
    with open(filename, 'r') as f:
        opened = json.load(f)
    return opened


def json_write(filename, data: dict):
    with open(filename, 'w') as f:
        json.dump(data, f)