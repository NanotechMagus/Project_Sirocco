#!/usr/bin/python3.7

# Standard Library Imports
import os
import json
import logging

# Locally Developed Imports

# Third Party Imports

# Initial variables
basePath = ""


# Initialization of base path for use in all classes
def __init__(key):
    global basePath

    basePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Class for reading JSON files within the core/data directory
class fileReader:

    def __init__(self, filetype: str, page: str):
        self.basePath = basePath
        self.datpath = os.path.join(self.basePath, filetype)
        self.datfile = os.path.join(self.datpath, page)

    # Private wrapper
    def __validate_file(self, func):
        def cvf(fullpath):
            return func() if os.path.exists(fullpath) else FileNotFoundError
        return cvf

    # Get data from specific page on call, return all info under key
    @__validate_file
    def get_data(self, keystore):
        try:
            data = json_open(self.datfile)
        except FileNotFoundError as err:
            errorHandler(err)
            return False
        else:
            return data[keystore]


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