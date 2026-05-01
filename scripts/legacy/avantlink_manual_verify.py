import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

gmail_user = 'booyajones222@gmail.com'
gmail_pass = os.environ.get('GMAIL_APP_PASSWORD', '')

msg = MIMEMultipart()
msg['From'] = formataddr(('errorcodefixes.com', gmail_user))
msg['To'] = 'affiliateapps@avantlink.com'
msg['Subject'] = 'Manual Application Verification Request - Application ID 1592329'
msg.attach(MIMEText(
    "Hi AvantLink team,\n\n"
    "I'm requesting manual verification for our affiliate application.\n\n"
    "Application ID: 1592329\n"
    "Website URL: https://errorcodefixes.com\n"
    "Email applied with: chris.a.wyatt@gmail.com\n\n"
    "The JavaScript verification tag is confirmed live in the page source at https://errorcodefixes.com "
    "(you can verify by viewing source and searching for 'avantlink' or 'application_id=1592329'). "
    "Our site is a static site hosted on Cloudflare Pages, which serves pre-built HTML. "
    "The tag loads correctly in real browsers but the automated verification appears to be timing out "
    "before the script executes.\n\n"
    "We're a technical reference site with 1,150+ fault code diagnostic guides for HVAC, "
    "commercial refrigeration, and industrial equipment. AirFilters.com is a natural fit for our "
    "content — nearly every HVAC article we publish includes filter replacement guidance.\n\n"
    "Please manually verify and approve application 1592329 at your earliest convenience.\n\n"
    "Thank you,\nMarcus Webb\nerrorcodefixes.com\ninfo@errorcodefixes.com",
    'plain'
))

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(gmail_user, gmail_pass)
    server.send_message(msg)
    print("Sent manual verification request to affiliateapps@avantlink.com")
