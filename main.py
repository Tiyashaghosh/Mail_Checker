import imaplib
import email
import os
import pandas as pd

my_email = "youremail@gmail.com"
app_password = "ypurapppassword"
imap_server = "imap.gmail.com" # Server you want to connect to

# Folder where attachments will be saved
download_folder = r"path where you wanna download the files"

with imaplib.IMAP4_SSL(imap_server) as imap:
    imap.login(my_email, my_password)
    imap.select("Inbox")

    _, email_ids = imap.search(None, 'From "specific email you want to read mails from"')

    for ids in email_ids[0].split():
        _, data = imap.fetch(ids, "(RFC822)")
        message = email.message_from_bytes(data[0][1])
        print("___________________________________________")
        print(f"From : {message.get('From')}")
        print(f"To : {message.get('To')}")
        print(f"Bcc : {message.get('Bcc')}")
        print(f"Date : {message.get('Date')}")
        print(f"Subject : {message.get('Subject')}")
        #
        for part in message.walk():
            # Print plain text email body
            if part.get_content_type() == "text/plain" and part.get('Content-Disposition') is None:
                body = part.get_payload(decode=True)
                print("Body:\n", body.decode(errors="ignore"))  # decoding to string

            # Handle attachments
            if part.get_content_disposition() == "attachment":             
                file_name = part.get_filename()
                print(file_name)
                if file_name and file_name.lower().endswith(".xlsx"):           # Scanning for specifc kind of file type here it is "xlsx".
                    file_path = os.path.join(download_folder, file_name)
                    print(file_path)
                    # Avoid overwriting if file already exists
                    if not os.path.exists(file_path) :
                        with open(file_path, "wb") as f:
                            f.write(part.get_payload(decode=True))             # Save the file to a specific folder
                        print(f" Attachment saved: {file_path}")

                    try:
                        df = pd.read_excel(file_path)
                        new_file_name = file_name.replace(".xlsx",".csv")             # Coverting from one file extension type to another using the try else block
                        new_path = os.path.join(download_folder,new_file_name)
                        df.to_csv(new_path,index=False)
                        print(f"New format: {new_path}")
                        os.remove(file_path)
                    except Exception as e:
                        print(f"Conversion failed : {e}")

