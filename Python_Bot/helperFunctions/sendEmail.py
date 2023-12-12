import smtplib
import imaplib
import email
from email.message import EmailMessage
from decouple import config

USER = config("EMAIL")
PASS = config("PASSWORD")
SMTPURL = config("SMTP_URL")
IMAPURL = config("IMAP_URL")

def sendEmail(to ,subject, content):
    email_sender = USER
    email_password = PASS
    email_receiver = to

    subject = subject
    body = content

    em = EmailMessage()
    em['FROM'] = email_sender
    em["TO"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    with smtplib.SMTP_SSL(SMTPURL, 465) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)

    print("Email Sent")

def readEmail():
    # connecting to imap server
    conn = imaplib.IMAP4_SSL(IMAPURL)
    conn.login(USER, PASS)

    # selecting the inbox
    conn.select('Inbox')

    # searching for all email's
    status, messages = conn.search(None, 'UNSEEN')
    msg_data= []
    #looping throught all mails
    for msg in messages[0].split():
        status, data = conn.fetch(msg, '(RFC822)')
        email_msg = email.message_from_bytes(data[0][1])

        msg_content = {
            "Subject": f"{email_msg['Subject']}",
            "From": f"{email_msg['From']}",
            "Date": f"{email_msg['Date']}",
            "Content": email_msg.get_payload()
        }

        print(msg_content)

        msg_data.append(msg_content)

    conn.close()
    conn.logout()

    return msg_data
