import datetime
import os.path
import json 
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar.events']
CredentialsD ={
    "installed": {
        "client_id": "710516965183-tpigp80bvoq0bu1b6gn14op18vsl9vlh.apps.googleusercontent.com",
        "project_id": "calyss-ia",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "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",
        "redirect_uris": [
            "http://localhost"
        ]
    }
}

def main(maildoctor , mailfarmer , date , title):
 
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("DemandeTraitement/token.json"):
        creds = Credentials.from_authorized_user_file("DemandeTraitement/token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "DemandeTraitement/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("DemandeTraitement/token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)
        event = {
            "summary": title,
            "location": "online",
            "description": "description",
            "colorId": "6",
            "start": {
                "dateTime": date ,
                "timeZone": "Africa/Tunis"
            },
            "end": {
                "dateTime": date,
                "timeZone": "Africa/Tunis"
            },
            "recurrence": [
                "RRULE:FREQ=DAILY;COUNT=1"
            ],
            "attendees": [
                {"email": maildoctor},
                {"email": mailfarmer}
            ]
        }
        event['start']['dateTime'] = str(event['start']['dateTime'])
        event['end']['dateTime'] = str(event['end']['dateTime'])

        event = service.events().insert(calendarId="primary", body=event).execute()
        event_json = json.dumps(event, indent=4)  # Format JSON with indentation for readability
        event_dict = json.loads(event_json)
        return event_dict['htmlLink']
    except HttpError as error:
        print(f"An error occurred: {error}")

# if __name__ == "__main__":
#     # Replace with actual emails, date, and title as needed
#     maildoctor = "yacinbnsalh@gmail.com"
#     mailfarmer = "wiem.benaraar@esprit.tn"
#     date = "2024-10-31T20:20:20+02:00"
#     title = "My Rendezvous"
#     event_json = main(maildoctor, mailfarmer, date, title)
#     # Parse the JSON string back to a dictionary
#       # Convert JSON string to a Python dictionary
    
#     # Print the HTML link if it exists
#     if 'htmlLink' in event_dict:
#         print()
    