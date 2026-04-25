from pathlib import Path
import re

p = Path(r"C:\Users\Administrator\.openclaw\workspace\industrial-fixes\src\data\blog")
files = [
    'ruud-upnl-heat-pump-error-codes.md',
    'ruud-ugph-error-codes.md',
    'ecosmart-eco27-error-codes.md',
    'ecosmart-eco36-error-codes.md',
    'eccotemp-i12-error-codes.md',
    'eccotemp-fvi12-error-codes.md',
    'takagi-tkjr2-error-codes.md',
    'friedrich-mini-split-error-codes.md',
    'american-standard-platinum-18-heat-pump-codes.md',
    'bosch-ids-2-heat-pump-error-codes.md',
]

for name in files:
    path = p / name
    txt = path.read_text(encoding='utf-8')
    body = re.sub(r'^---\n.*?\n---\n', '', txt, flags=re.S)
    words = len(re.findall(r"\b\w+[\w'-]*\b", body))
    print(f"{name}\tEXISTS={path.exists()}\tWORDS={words}")
