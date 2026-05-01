import smtplib, time, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

gmail_user = 'booyajones222@gmail.com'
gmail_pass = os.environ.get('GMAIL_APP_PASSWORD', '')

targets = [
    {
        "to": "info@acca.org",
        "subject": "Free technical resource for HVAC contractor members - fault code diagnostic guides",
        "body": (
            "Hi ACCA team,\n\n"
            "I wanted to reach out about a free technical resource that may be useful for your contractor members.\n\n"
            "errorcodefixes.com provides 1,150+ free fault code diagnostic guides covering the equipment your members "
            "service daily - Carrier, Trane, Lennox, Goodman, Rheem, and 30+ other brands. Each guide covers what "
            "the code means, diagnostic sequence, parts typically needed, and when to escalate.\n\n"
            "We're not selling anything - it's a free reference site used by technicians and homeowners. "
            "If ACCA maintains any member resource pages or 'useful links' sections, we'd be grateful "
            "to be included. We're also open to any partnership or content collaboration if that's ever relevant.\n\n"
            "Thank you for the work ACCA does for the industry.\n\n"
            "Best,\nMarcus Webb\nerrorcodefixes.com\ninfo@errorcodefixes.com"
        )
    },
    {
        "to": "rses@rses.org",
        "subject": "Free fault code reference resource for RSES members",
        "body": (
            "Hi RSES team,\n\n"
            "I'm reaching out about a free technical resource that may benefit your refrigeration and HVAC members.\n\n"
            "errorcodefixes.com provides 1,150+ fault code diagnostic guides covering HVAC, commercial refrigeration "
            "(Hoshizaki, Manitowoc, Scotsman, True), VFDs, and related equipment. Every guide is written at the "
            "technician level - diagnostic sequences, not just code definitions.\n\n"
            "We cover commercial refrigeration extensively: walk-in coolers, reach-in cases, ice machines, and "
            "condensing units. Given RSES's focus on refrigeration service professionals, this seems like a natural fit.\n\n"
            "If you maintain a resources page or member reference links, we'd love to be included. "
            "Happy to provide any additional information.\n\n"
            "Best,\nMarcus Webb\nerrorcodefixes.com\ninfo@errorcodefixes.com"
        )
    },
    {
        "to": "nate@natex.org",
        "subject": "Free technical reference resource for NATE-certified technicians",
        "body": (
            "Hi NATE team,\n\n"
            "I wanted to introduce a free technical resource that NATE-certified technicians may find useful in the field.\n\n"
            "errorcodefixes.com has 1,150+ fault code diagnostic guides for HVAC and refrigeration equipment - "
            "covering the brands your certified technicians service most: Carrier, Trane, Lennox, Rheem, Goodman, "
            "Daikin, Mitsubishi, and more. Our authors include EPA 608 and NATE-certified technicians.\n\n"
            "The guides are free, no registration required, and structured for rapid field use - "
            "quick code lookup with full diagnostic sequences.\n\n"
            "If NATE ever recommends field reference tools to certified technicians or maintains any resource "
            "listings, we'd be honored to be considered.\n\n"
            "Best,\nMarcus Webb\nerrorcodefixes.com\ninfo@errorcodefixes.com"
        )
    },
    {
        "to": "info@phccweb.org",
        "subject": "Free fault code resource for plumbing and HVAC contractor members",
        "body": (
            "Hi PHCC team,\n\n"
            "I wanted to flag a free technical resource that may be useful for your plumbing, heating, "
            "and cooling contractor members.\n\n"
            "errorcodefixes.com provides 1,150+ fault code guides covering tankless water heaters (Navien, "
            "Rinnai, Noritz, Bradford White), boilers, and HVAC systems. Each guide is designed for working "
            "technicians - diagnostic sequences, parts lists, and safety thresholds.\n\n"
            "The site is completely free to use. If PHCC maintains any technical resource pages for members, "
            "we'd appreciate being included.\n\n"
            "Best,\nJames Rutherford\nerrorcodefixes.com\ninfo@errorcodefixes.com"
        )
    },
    {
        "to": "info@ashrae.org",
        "subject": "Technical resource suggestion - HVAC fault code diagnostic reference",
        "body": (
            "Hi ASHRAE team,\n\n"
            "I wanted to bring a free technical resource to your attention for potential inclusion "
            "in ASHRAE member resources or bookshelf recommendations.\n\n"
            "errorcodefixes.com provides 1,150+ fault code diagnostic guides covering HVAC, "
            "commercial refrigeration, and building automation equipment. The site targets "
            "HVAC/R practitioners who need field-level diagnostic sequences rather than general reference text.\n\n"
            "Content is based on OEM service literature and written by EPA 608 and NATE-certified technicians. "
            "It covers equipment categories relevant to ASHRAE standards including refrigerants, "
            "heat pumps, and commercial cooling systems.\n\n"
            "If ASHRAE maintains any practitioner resource listings, we'd welcome the consideration.\n\n"
            "Best,\nMarcus Webb\nerrorcodefixes.com\ninfo@errorcodefixes.com"
        )
    }
]

sent = []
failed = []
for t in targets:
    try:
        msg = MIMEMultipart()
        msg['From'] = formataddr(('errorcodefixes.com', gmail_user))
        msg['To'] = t['to']
        msg['Subject'] = t['subject']
        msg.attach(MIMEText(t['body'], 'plain'))
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(gmail_user, gmail_pass)
            server.send_message(msg)
        sent.append(t['to'])
        time.sleep(3)
    except Exception as e:
        failed.append(f"{t['to']}: {e}")

print("Sent:", sent)
print("Failed:", failed)
