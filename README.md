# 📩 Email Attachment Downloader & Converter

This Python automation script connects to your Gmail inbox, scans for messages from specific senders, downloads Excel `.xlsx` attachments, converts them to CSV format, and optionally sends the converted file back to the original sender.

---

## 🚀 Features

- Secure Gmail access using **IMAP**
- Filters emails by a **specific sender**
- Detects and downloads `.xlsx` file attachments
- Converts `.xlsx` files to `.csv` using **Pandas**
- Automatically sends back the converted file via **SMTP**
- Saves files to a defined local directory
- Skips already downloaded files to avoid duplicates
- Environment variable support for secure credentials

🔧 Tech Stack
Python 3.x
imaplib, email – Accessing and parsing emails
smtplib, email.message – Sending emails with attachments
pandas, openpyxl – Excel to CSV conversion
os – File and directory handling
dotenv – Securely load credentials from .env
