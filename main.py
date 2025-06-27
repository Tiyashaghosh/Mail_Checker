import imaplib
import email

my_email = "your_email@gmail.com"
my_password = "your_password"
imap_server = "imap.gmail.com" # Server you want to connect to


with imaplib.IMAP4_SSL(imap_server) as imap:
    imap.login(user= my_email,password=my_password)
    imap.select("inbox")
    _,msgnums = imap.search(None,"ALL") # here "_" signifies the status if the code ran successfully

    for msgnum in msgnums[0].split(): # here we get the data as [b '1 2 3 4'] so need to spilt it
        _,data = imap.fetch(msgnum,"(RFC822)")
        message = email.message_from_bytes(data[0][1])

        print(f"Message Number: {msgnum}")
        print(f"From : {message.get('From')}")
        print(f"To : {message.get('To')}")
        print(f"Bcc : {message.get('Bcc')}")
        print(f"Date : {message.get('Date')}")
        print(f"Subject : {message.get('Subject')}")
        print("\n")

        print("Contents:")
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                print(part.as_string())
