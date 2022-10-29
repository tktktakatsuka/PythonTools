from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json
import base64


def get_header(headers , name):
    for h in headers:
        if h['name'].lower()  == name:
            return h['value']


def base64_decode(data):
    return base64.urlsafe_b64decode(data).decode()

def get_body(body):
    if body['size'] > 0 :
        return base64_decode(body['data'])

def get_parts_body(body):
    if(body['size'] > 0
        and 'data' in body.keys()
        and 'mimeType' in body.keys()
        and body['mimeType'] == 'text/plain'
    ) :
        return base64_decode(body['data'])


def get_parts(parts):
    for part in parts:
        if part['mimeType'] == 'text/plain':
            b = base64_decode(part['body']['data'])
            if b is not None:
                return b
            
        if 'body' in part.keys():
            b = get_parts_body(part['body'])
            if b is not None:
                return b

        if 'parts' in part.keys():
            b = get_parts_body(part['parts'])
            if b is not None:
                return b
        



def main():
    scopes = ['https://mail.google.com/']
    creds = Credentials.from_authorized_user_file('token.json', scopes)
    service = build('gmail','v1', credentials=creds)

    messages = service.users().messages().list(
        userId= 'me'
        
    ).execute().get('messages')

    for message in messages:
        print('=' *10)
        m_data = service.users().messages().get(
                userId= 'me' ,
                id = message['id']
        ).execute()

        #ヘッダー情報
        body = m_data['payload']['body']
        body_data = get_body(body)
        parts_data = None

        if 'parts' in m_data['payload'].keys():
            parts = m_data['payload']['parts']
            parts_data = get_parts(parts)
        
        body_result = body_data if body_data is not None else parts_data
        print(f'本文: {body_result}')




if __name__ == '__main__':
    main()
