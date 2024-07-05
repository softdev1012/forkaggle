import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up the sender and recipient email addresses
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@example.com"

# Create a MIMEMultipart message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Subject of the email"

# Add email content
email_content = "This is the email content sent from Python"
message.attach(MIMEText(email_content, "plain"))

# Connect to Gmail's SMTP server
smtp_server = "smtp.gmail.com"
port = 587
username = "your_email@gmail.com"
password = "your_password"

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(username, password)
    
    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())