import requests 

domain = input("Enter URL: ")

pages = [
    "/security",
    "/bugbounty",
    "/.well-known/security.txt",
    "/responsible-disclosure"
]

def get_text(url):
    try:
        r = requests.get(url, timeout=3)
        return r.status_code, r.text
    except:
        return None, ""

# fake page (outside function)
_, fake = get_text("https://" + domain + "/abcd1234")

for page in pages:
    url = "https://" + domain + page
    status, text = get_text(url)

    if status and status != 404 and text != fake:
        print(f"[FOUND] {url} -> {status}")
    else:
        print(f"[NOT FOUND] {url}")