#0. Import essentials libraries
import markdown_it
from twilio.rest import Client
from datetime import datetime, timedelta
import time
import streamlit as st
import pandas as pd

#Setup Twilio
account_sid = ["twilio"]["account_sid"]
auth_token = ["twilio"]["auth_token"]

client = Client(account_sid, auth_token)

#send message function
def send_message(number, message):
    try:
        msg = client.messages.create(
            from_=[twilio][whatsapp_no],
            body=message,
            to = f'whatsapp:{number}'
        )
        print(f'Messages sent successfully')
    
    except Exception as e:
        print('An error occured')


#UI code
# --- PAGE CONFIG ---
st.set_page_config(page_title="WhatsApp Automation Tool", page_icon="💬", layout="centered")

# --- HEADER ---
st.title("💬 WhatsApp Automation Tool")
st.markdown("Easily send personalized WhatsApp messages by uploading an Excel file!")

# --- FILE UPLOAD SECTION ---
name = st.text_input('Enter the Name of user: ')
no = st.text_input('Enter the receiptent number: ')
msg_body = st.text_input('enter the message u want to send')

date_str = st.text_input('Enter the date to send the message(YYYY/MM/DD): ')
time_str = st.text_input('Enter thr time to send (HH:MM): ')

recip_no = '+91' + no

if st.button('Enter to send Msg'):
    schedule_date = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
    current_datetime = datetime.now()

    time_diffn = schedule_date - current_datetime
    delay_sec = time_diffn.total_seconds()

    if delay_sec <= 0:
        print('the time is invalid')
    else:
        print(f'Message scheduled to send at {schedule_date}')



        #4. Send Message
        time.sleep(delay_sec)
        send_message(recip_no, msg_body)
        st.success(f"Message scheduled to send at {schedule_date}")
