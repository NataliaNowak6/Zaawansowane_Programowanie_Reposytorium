import requests

def load_from_url(url, path):
    r = requests.get(url)
    with open(path, "wb") as f:
        f.write(r.content)