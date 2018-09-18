import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import Config

def parse_email():
    email = "<html><head></head><body>"
    email += "<h1>Commit Feedback!</h1>\n"

    toolchain_output = ""
    with open("logs/log-toolchain.txt", 'r') as file:
        toolchain_output = file.read()

    simulation_output = ""
    with open("logs/log-simulation.txt", 'r') as file:
        simulation_output = file.read()

    # Loop through all people
    email += "<h2>Toolchain Output</h2>"
    email += toolchain_output.replace('\n', '<br>') + "<br>"

    email += "<h2>Simulation Output</h2>"
    email += simulation_output.replace('\n', '<br>') + "<br>"

    email += "<i>With love,<br>\nCubeBot</i>"
    email += "</body></html>"

    print(email)

    return email


def send_email(content):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(Config.EMAIL, Config.EMAIL_PASSWORD)

    me = Config.EMAIL
    you = Config.TARGET_EMAIL

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Latest Commit Feedback"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hello World!"
    html = content

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    server.sendmail(me, [Config.TARGET_EMAIL], msg.as_string())
    server.quit()

email_text = parse_email()
send_email(email_text)