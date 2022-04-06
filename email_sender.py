from support import Create_Service
import get_data
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Executes the main() function to retrieve the data from the news API and create our text file
get_data.main()

client_secret_file = 'client_secret_file.json'
api_name = 'gmail'
api_version = 'v1'
scopes = ['https://mail.google.com/']

service = Create_Service(client_secret_file, api_name, api_version, scopes)

emailMsg = f"""Hello!

See below today's top news:

{get_data.data_as_string}

Have a great day!
""" 

recipients = ['receiversEmailAddress'] # Flag 2
mimeMessage = MIMEMultipart()
mimeMessage['to'] = ", ".join(recipients)
mimeMessage['subject'] = f"{get_data.date} top 20 headlines"
mimeMessage.attach(MIMEText(emailMsg, 'plain'))
raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
print(message)