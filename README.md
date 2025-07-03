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
Python 3.x – Core programming language used to automate email processing and file handling.

imaplib – Connects to Gmail using IMAP to read and filter emails.

email – Parses email content and extracts body and attachments.

smtplib – Sends emails via SMTP, used to reply with the converted files.

email.message.EmailMessage – Builds structured MIME emails with attachments.

pandas – Converts .xlsx files to .csv, enabling flexible data manipulation.

openpyxl – Excel engine used by pandas to read .xlsx files.

os – Manages file paths, creates and removes files, checks file existence.

python-dotenv – Loads email credentials securely from a .env file.


