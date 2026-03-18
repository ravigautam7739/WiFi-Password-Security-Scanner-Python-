import time
import re
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

print("WiFi Password Security Scanner")
print("--------------------------------")

password = input("\nEnter WiFi Password: ")

clear()

print("Scanning password...\n")
time.sleep(2)

score = 0

# length
if len(password) >= 8:
    print("Length Check: PASS")
    score += 1
else:
    print("Length Check: FAIL")

# numbers
if re.search(r"\d", password):
    print("Numbers Detected: PASS")
    score += 1
else:
    print("Numbers Detected: FAIL")

# uppercase
if re.search(r"[A-Z]", password):
    print("Uppercase Letters: PASS")
    score += 1
else:
    print("Uppercase Letters: FAIL")

# special characters
if re.search(r"[!@#$%^&*]", password):
    print("Special Characters: PASS")
    score += 1
else:
    print("Special Characters: FAIL")

print()
if score <= 1:
    print("Security Level: VERY WEAK ❌")
    print("Estimated crack time: seconds")

elif score == 2:
    print("Security Level: WEAK ⚠️")
    print("Estimated crack time: minutes")

elif score == 3:
    print("Security Level: MEDIUM")
    print("Estimated crack time: days")

else:
    print("Security Level: STRONG 🔐")
    print("Estimated crack time: years")