import speedtest
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import json

with open('config.json') as config_file:
    config = json.load(config_file)

from_email = config["from_email"]
from_password = config["from_password"]
to_email = config["to_email"]
speed_threshold = config["speed_threshold"]

recipient_name = to_email.split('@')[0].split('.')[0].capitalize()

def send_email(download_speed):
    subject = "🚨 Alert! Your Internet Speed Needs a Boost! 🚀"
    body = f"""\
    Hi {recipient_name},

    Looks like your internet is taking a little coffee break! ☕️ Your current download speed is {download_speed:.2f} Mbps, 
    which is below the threshold of {speed_threshold} Mbps that you set.

    Your internet might need a little boost. 🏃‍♂️💨

    Stay connected,
    NetSpeedFox
    """

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Internet Dropped - > Email sent successfully.")
    except Exception as e:
        print(f"Internet Dropped - > Failed to send email: {e}")

def check_internet_speed():
    try:
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        results = st.results.dict()
        download_speed_mbps = results["download"] / 1_000_000
        print(f"Your Internet Download speed: {download_speed_mbps} Mbps")
        if download_speed_mbps < speed_threshold:
            send_email(download_speed_mbps)
    except Exception as e:
        print(f"Failed to perform speed test: {e}")
        send_email(0)

def run_schedule():
    schedule.every(1).minutes.do(check_internet_speed)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    run_schedule()
