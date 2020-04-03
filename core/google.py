#!/usr/bin/python3.7

# Standard Library Imports
import datetime
import pickle
import os.path

# Locally Developed Imports

# Third Party Imports
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.


class gcal:

    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
        self.__creds = None
        self.__calID = None
        if os.path.exists('./conf/token.pickle'):
            with open('./conf/token.pickle', 'rb') as token:
                self.__creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.__creds or not self.__creds.valid:
            if self.__creds and self.__creds.expired and self.__creds.refresh_token:
                self.__creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    './conf/client_secret.json', self.SCOPES)
                self.__creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('./conf/token.pickle', 'wb') as token:
                pickle.dump(self.__creds, token)
        self.service = build('calendar', 'v3', credentials=self.__creds)
        # Get Calendar ID from list
        if not self.__calID:
            self.__calID = self.service.calendarList().list().execute()['items'][1]['id']

    def get_cal(self, maxr=10):
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = self.service.events().list(
            calendarId=self.__calID,
            timeMin=now,
            maxResults=maxr,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])

        eventreturn = {}
        eventreturnx = []
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            if not event['summary'] in eventreturn.values():
                eventreturn[start] = event['summary']
                eventreturnx.append(f"{start} - {event['summary']}")

        return eventreturnx
