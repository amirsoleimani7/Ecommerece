from django.shortcuts import render, redirect
import os
import json
from django.urls import reverse
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow


CLIENT_SECRET_FILES = os.path.join(settings.BASE_DIR , 'cred.json')

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

REDIRECT_URI = 'http://localhost:8000/google/callback/'

def home(request):
    return HttpResponse("welcome! <a href='/google/login/'> Loging with google </a>")


def google_login(request):
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILES ,SCOPES)
    flow.redirect_uri = 'http://localhost:8000/google/callback/'

    authorization_url, state = flow.authorization_url(access_type='offline', prompt='consent')

    request.session['state'] = state
    
    return redirect(authorization_url)

def google_callback(requeset):
    
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,
    )
    flow.fetch_token(authentication_respone=requeset.build_absolute_uri())

    credentials = flow.credentials
    service = build('gamil' , 'v1' , credentials=credentials)

    # fetching the messages
    result = service.users().message().list(userId='me' , maxResults=5).execute()
    messages = result.get('messages' , [])
    

    email_data = []
    for msg in messages:
        msg_detail = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_detail['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
        snippet = msg_detail.get('snippet', '')
        email_data.append({
            'subject': subject,
            'sender': sender,
            'snippet': snippet,
    })

    return render(requeset , 'google_auth_mode/emails.html' , {'emails' : email_data})

def fetch_emails(request):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        return HttpResponse("No valid credentials. Please log in first.")
    service = build('gmail', 'v1', credentials=creds)

    try:
        results = service.users().messages().list(userId='me', maxResults=5).execute()
        messages = results.get('messages', [])

        email_subjects = []
        if not messages:
            email_subjects.append('No messages found.')
        else:
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                snippet = msg.get('snippet', '(No snippet)')
                email_subjects.append(snippet)
        return HttpResponse('<br><br>'.join(email_subjects))
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")
