import smtplib, time, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

gmail_user = 'booyajones222@gmail.com'
gmail_pass = os.environ.get('GMAIL_APP_PASSWORD', '')

targets = [
    {
        "to": "info@hvactoolkit.org",
        "subject": "Resource suggestion - comprehensive error code guides for your users",
        "body": (
            "Hi HVAC Toolkit team,\n\n"
            "I came across your error code database and wanted to flag a resource that complements what you're doing.\n\n"
            "errorcodefixes.com has 1,150+ in-depth fault code guides covering HVAC, commercial refrigeration, VFDs, and CNC equipment. "
            "Where your database gives quick code lookups, our articles provide full diagnostic sequences - step-by-step procedures, "
            "parts lists, and when-to-call-a-tech guidance.\n\n"
            "Example: your Carrier 13 entry shows \"Limit circuit fault.\" Our page at "
            "https://errorcodefixes.com/posts/carrier-13-error-code/ walks through exactly how to diagnose whether it's the "
            "heat exchanger, airflow, or limit switch, with specific resistance checks.\n\n"
            "If you ever link to external resources on your site, we'd be honored to be included. "
            "Either way, thought it might be useful for your users.\n\n"
            "Best,\nMarcus Webb\nerrorcodefixes.com\ninfo@errorcodefixes.com"
        )
    },
    {
        "to": "contact@heatinghelp.com",
        "subject": "Resource for your forum members - fault code diagnostic guides",
        "body": (
            "Hi Heating Help team,\n\n"
            "We see constant questions on HVAC forums about specific fault codes with no good online reference. "
            "We built errorcodefixes.com to fill that gap - 1,150+ articles covering furnace flash codes, "
            "heat pump fault codes, boiler errors, and tankless water heater codes.\n\n"
            "Each article goes past the code definition to the diagnostic sequence, parts likely needed, "
            "and the safety threshold where you call a pro.\n\n"
            "A few examples:\n"
            "- Inducer pressure switch faults (covers condensate drain vs. cracked HX differentiation)\n"
            "- Navien tankless E003/E004 codes (step-by-step gas pressure verification)\n"
            "- Bradford White water heater blink codes\n\n"
            "If you have a resources section or ever recommend external sites to your members, we'd love to be included.\n\n"
            "Best,\nJames Rutherford\nerrorcodefixes.com\ninfo@errorcodefixes.com"
        )
    },
    {
        "to": "admin@hvac-talk.com",
        "subject": "Offering errorcodefixes.com as a resource for members",
        "body": (
            "Hi HVAC-Talk admin,\n\n"
            "We run errorcodefixes.com - a technical reference site with 1,150+ fault code guides covering "
            "HVAC, VFDs, commercial refrigeration, and CNC equipment.\n\n"
            "Every day on forums like yours, members ask questions like 'Carrier 3 flashes - what does it mean?' "
            "or 'Navien E003 code - where do I start?' We have dedicated diagnostic articles for thousands of "
            "these exact queries, written at the technician level.\n\n"
            "We'd love to be referenced in your resources section, sticky threads, or anywhere your moderators "
            "think it would help members. We're happy to create brand-specific pages on request if there are "
            "common code questions we're missing.\n\n"
            "Best,\nMarcus Webb\nerrorcodefixes.com\ninfo@errorcodefixes.com"
        )
    },
    {
        "to": "editors@doityourself.com",
        "subject": "Resource suggestion for your HVAC troubleshooting section",
        "body": (
            "Hi DoItYourself.com editorial team,\n\n"
            "I wanted to bring errorcodefixes.com to your attention as a potential resource link for your HVAC "
            "and home repair sections.\n\n"
            "We have 1,150+ articles covering specific error codes across major HVAC brands (Carrier, Trane, "
            "Lennox, Goodman, Rheem), water heaters (Navien, Bradford White, Rinnai), and more. "
            "The articles target the exact moment of panic - someone's furnace stopped working and their "
            "thermostat is showing a code they don't understand.\n\n"
            "Given that your audience is DIY homeowners dealing with exactly these situations, "
            "a mention or link in relevant articles could genuinely help your readers.\n\n"
            "Happy to provide specific article URLs for any equipment categories you cover.\n\n"
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
