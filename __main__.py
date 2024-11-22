import pytesseract
from PIL import Image
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['']
CREDENTIALS_FILE = '' #Add JSON File For Credentials

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPES)
service = build('sheets', 'v4', credentials=credentials)
spreadsheet_id = ''


image_path = './11111.jpeg'

text = pytesseract.image_to_string(Image.open(image_path))


rows = []
for line in text.splitlines():
    # Split the line by the most common delimiter 
    parts = line.split(' ')

    if len(parts) >= 3 and any(part.startswith('US') for part in parts):
        row = {
            'GUSA-Ya': parts[0] if parts[0].startswith('GUSA-Ya') else '',
            'Name': parts[1] if parts[1].startswith('Leonroni') else '',
            'Day': parts[2].split('/')[1] if '/' in parts[2] else '',
            'Month': parts[2].split('/')[0] if '/' in parts[2] else '',
            'Year': parts[2].split('/')[2] if '/' in parts[2] else '',
            'Time': parts[3] if ':' in parts[3] else '',
            'Phone': parts[4] if '(' in parts[4] else '',
            'Street': parts[5] if 'St.' in parts[5] or 'Rd.' in parts[5] else '',
            'City': parts[6] if parts[6].endswith('Rd324') or parts[6].endswith('Consir') else '',
            'State': parts[7] if parts[7] == 'US' else '',
            'Zip': parts[8