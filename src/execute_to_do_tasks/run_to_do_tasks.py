import shutil
import os
import re
import smtplib
import traceback
import yfinance as yf
from datetime import datetime
from email.mime.text import MIMEText
from typing import List, Dict
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from apscheduler.schedulers.background import BackgroundScheduler
from ics import Calendar, Event

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import Dict, List

from dotenv import load_dotenv

load_dotenv()

API_KEYS = {
    'alpha_vantage_api_key': os.getenv('alpha_vantage_api_key')
}

EMAIL_CREDS = {
    'email': os.getenv('EMAIL_ADDRESS'),
    'password': os.getenv('PASSWORD')
}



#---------------------
# Notification System
#---------------------

def send_email(subject: str, body: str, recipient: str) -> None:
    """
    Send email using SMTP.
    
    Example call:
    send_email("Important Notice", "This is an important message", "recipient@example.com")

    Args:
        subject (str): Email subject
        body (str): Email body content
        recipient (str): Recipient email address

    Returns:
        None: Function does not return a value

    Raises:
        Exception: If email sending fails
    """

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_CREDS['email']
    msg['To'] = recipient

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_CREDS['email'], EMAIL_CREDS['password'])
            server.send_message(msg)
    except smtplib.SMTPException as e:
        raise Exception(f"Email failed to send: {str(e)}")




def send_calendar_invite(event_title, event_time, to_emails, location="online"):
    """
    Create and send a calendar invite via email
    
    Example call:
    send_calendar_invite("Team Meeting", "2024-06-24T14:00:00", ["person@example.com"], "Conference Room A")
    
    Args:
        event_title (str): Title of the calendar event
        event_time (str): Time of the event in ISO format
        to_emails (list): List of recipient email addresses
        location (str, optional): Location of the event. Defaults to "online"
        
    Returns:
        str: Confirmation message or error details of the calendar invite operation
    """
    pat = re.search(r"\d+\/\d+\/\d+", event_title) 

    if pat is None:
        event_date = ""
    else:
        event_date = pat.group()

    from_email = EMAIL_CREDS.get("email")
    email_password = EMAIL_CREDS.get("password")

    # Create calendar event
    calendar = Calendar()
    event = Event()
    event.name = event_title
    
    # Convert date string to datetime
    # start_time = datetime.strptime(f"{event_date} 09:00:00", "%Y-%m-%d %H:%M:%S")
    # end_time = datetime.strptime(f"{event_date} 10:00:00", "%Y-%m-%d %H:%M:%S")
    
    event.begin = "2025-03-05 17:15:00"
    event.end = "2025-03-05 18:45:00"
    event.location = location
    
    calendar.events.add(event)
    
    # Save the calendar to a file temporarily
    with open('invite.ics', 'w') as f:
        f.write(str(calendar))
    
    # Create email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = f"Calendar Invite: {event_title}"
    
    body = f"You are invited to {event_title} on {event_date} at {event_time}, {location}"
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach the calendar file
    attachment = open('invite.ics', 'rb')
    part = MIMEBase('text', 'calendar', method="REQUEST", name="invite.ics")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="invite.ics"')
    msg.attach(part)
    
    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, email_password)
        text = msg.as_string()
        server.sendmail(from_email, to_emails, text)
        server.quit()
        print("Calendar invite sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")



def get_stock_price(symbol: str) -> str:
    """
    Get current stock price using Alpha Vantage API.
    
    Example call:
    get_stock_price("AAPL")

    Args:
        symbol (str): Stock ticker symbol

    Returns:
        str: Formatted stock information with price and change percentage

    Raises:
        Exception: If API request fails
    """
    try:
        ticker = yf.Ticker("NVDA")
        
        # Get the ticker info
        info = ticker.info
        
        # Extract relevant information
        price = info.get('regularMarketPrice', 'N/A')
        change_percent = info.get('regularMarketChangePercent', 'N/A')
        
        # Format change percent if available
        if change_percent != 'N/A':
            change_percent = f"{change_percent:.2f}%"
        return f"""
        {symbol} Stock Update:
        Price: ${price}
        Change: {change_percent}
        """
    except Exception as e:
        raise Exception(f"Stock data fetch failed: {str(e)}")


#-------------------
# Scheduler System
#-------------------

def setup_scheduler():
    """
    Configure background scheduler for recurring tasks.
    
    Example call:
    scheduler = setup_scheduler()
    
    Args:
        None: This function takes no arguments
        
    Returns:
        BackgroundScheduler: Initialized scheduler instance ready for adding jobs
    """
    scheduler = BackgroundScheduler()
    scheduler.start()
    return scheduler


#-------------------
# Main Controller
#-------------------

def process_todo_file(folder_path: str) -> None:
    """
    Main function to process todo.txt and execute commands.
    
    Example call:
    process_todo_file("/path/to/todo.txt")

    Args:
        file_path (str): Path to todo.txt file
        
    Returns:
        None: This function does not return a value
    """
    commands = []
    patterns = {
        'email_reminder': r'Remind me to (.*?) via email',
        'calendar_invite': r'Add a calendar invite for (.*?) date at (.*?) and share it with "(.*?)"',
        'stock_alert': r'Share the stock price for (.*?) every day at (.*?) via email with me'
    }
    file_path = os.path.join(folder_path, "to_do.txt")

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            for cmd_type, pattern in patterns.items():
                match = re.match(pattern, line)
                if match:
                    commands.append({
                        'type': cmd_type,
                        'params': match.groups()
                    })
                    break

    scheduler = setup_scheduler()

    for cmd in commands:
        print(cmd)
        print()
        try:
            if cmd['type'] == '1email_reminder':
                message = cmd['params'][0]
                send_email(
                    subject="Reminder Notification",
                    body=f"Reminder: {message}",
                    recipient=EMAIL_CREDS['email']
                )

            elif cmd['type'] == 'calendar_invite':
                event_title, event_time, attendees = cmd['params']
                event_id = send_calendar_invite(
                    event_title=event_title,
                    event_time=event_time,
                    to_emails=[attendees]
                )

            elif cmd['type'] == 'stock_alert':
                symbol, time_str = cmd['params']

                time_parts = time_str.split(':')
                if len(time_parts) != 2:
                    raise ValueError(f"Invalid time format: {time_str}. Expected format HH:MM")
                    
                hour = int(time_parts[0])
                minute = int(time_parts[1])
                scheduler.add_job(
                    lambda: send_email(
                        subject=f"{symbol} Stock Update",
                        body=get_stock_price(symbol),
                        recipient=EMAIL_CREDS['email']
                    ),
                    'cron',
                    hour=hour,
                    minute=minute
                )

        except Exception as e:
            print(f"Failed to process command: {str(traceback.format_exc(e))}")