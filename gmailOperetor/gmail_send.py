from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

def message_base64_encode(message):
    return base64.urlsafe_b64encode(message.as_bytes()).decode()


def main():
    scopes = ['https://mail.google.com/']
    creds = Credentials.from_authorized_user_file('token.json', scopes)
    service = build('gmail','v1', credentials=creds)

    message = MIMEText('testmimet')
    message['To'] = 'blue.mountain.syota@gmail.com'
    message['From'] = 'blue.mountain.syota@gmail.com'
    message['subject'] = 'test'


    raw = {'raw': message_base64_encode(message)}
    service.users().messages().send(
        userId='me',
        body=raw
    ).execute()
    




if __name__ == '__main__':
    main()