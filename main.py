import imaplib
import email
import os
import pandas as pd
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv('.env')
my_email: str = os.getenv('EMAIL')
my_password: str = os.getenv('APP_PASSWORD')

imap_server = "imap.gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 465

download_folder = r"path\to\your\download\folder"

def send_email_with_attachment(to_email, subject, body, attachment_path):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = my_email
    msg['To'] = to_email
    msg.set_content(body)

    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)
        msg.add_attachment(file_data, maintype='text', subtype='csv', filename=file_name)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
        smtp.login(my_email, my_password)
        smtp.send_message(msg)
        print(f"Email sent with attachment: {file_name}")

with imaplib.IMAP4_SSL(imap_server) as imap:
    imap.login(my_email, my_password)
    imap.select("Inbox")

    _, email_ids = imap.search(None, 'FROM "specific@email.com"')

    for ids in email_ids[0].split():
        _, data = imap.fetch(ids, "(RFC822)")
        message = email.message_from_bytes(data[0][1])
        print("___________________________________________")
        print(f"From    : {message.get('From')}")
        print(f"To      : {message.get('To')}")
        print(f"Bcc     : {message.get('Bcc')}")
        print(f"Date    : {message.get('Date')}")
        print(f"Subject : {message.get('Subject')}")

        for part in message.walk():
            if part.get_content_type() == "text/plain" and part.get('Content-Disposition') is None:
                body = part.get_payload(decode=True)
                print("Body:\n", body.decode(errors="ignore"))

            if part.get_content_disposition() == "attachment":
                file_name = part.get_filename()
                print("Attachment found:", file_name)

                if file_name and file_name.lower().endswith(".xlsx"):
                    file_path = os.path.join(download_folder, file_name)
                    if not os.path.exists(file_path):
                        with open(file_path, "wb") as f:
                            f.write(part.get_payload(decode=True))
                        print(f"Saved: {file_path}")

                    try:
                        df = pd.read_excel(file_path)
                        new_file_name = file_name.replace(".xlsx", ".csv")
                        new_path = os.path.join(download_folder, new_file_name)
                        df.to_csv(new_path, index=False)
                        print(f"Converted to CSV: {new_path}")

                        sender_email = email.utils.parseaddr(message.get('From'))[1]
                        send_email_with_attachment(
                            to_email=sender_email,
                            subject=f"Converted File: {new_file_name}",
                            body="Please find the converted CSV file attached.",
                            attachment_path=new_path
                        )

                        os.remove(file_path)
                        os.remove(new_path)

                    except Exception as e:
                        print(f"Conversion failed: {e}")
