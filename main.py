import regular_expressions as regex
import re

strings: list[str] = [
    "“The internal network is composed of several services.",
    "Web server is running at 172.0.5.20.",
    "Database server is running at 10.0.5.20",
    "Backup is available through 172.0.5.40",
    "Monitoring is operating at 85.12.30.7",
    "Whitelist for access contains range from 200.14.4.1 to 200.14.4.100"
]
text = "\n".join(strings)

ip_pattern = regex.ipv4_pattern()
for mo in re.finditer(ip_pattern, text):
    print(mo.group())