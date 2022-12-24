import re

value = "Hi, there I'm sushant"

output = re.search("^This.*string$", value)
print(output)

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"


# =============================================================
# Meaning of []  symbol in python
# []	A set of characters
# individually listing takes palce ex: [Sushant] will mathch  'S','U','S','H','A','N','T'
#

