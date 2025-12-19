import requests

SHORTENER_API = "https://dl.jaraflix.com/api/shorten/"


def shorten_url(long_url, title=None):
    try:
        res = requests.post(
            SHORTENER_API,
            json={
                "url": long_url,
                "title": title
            },
            timeout=10
        )

        data = res.json()
        if res.status_code == 200 and "short_url" in data:
            return data["short_url"]

    except Exception:
        pass

    return long_url
