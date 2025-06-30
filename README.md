# 📩 Email Attachment Downloader & Converter

This Python automation script connects to your email inbox, scans for messages from specific senders, downloads Excel (.xlsx) attachments, and converts them to CSV format.

---

## 🚀 Features

- Connects securely to Gmail using IMAP
- Filters emails by sender 
- Detects and downloads .xlsx attachments
- Automatically converts .xlsx files to .csv
- Saves converted files to a local folder
- Avoids duplicate downloads
- Easy to configure and extend

---

## 🔧 Tech Stack

- Python 3.x
- imaplib, email – for email access
- pandas, openpyxl – for Excel to CSV conversion
- os – for file handling
