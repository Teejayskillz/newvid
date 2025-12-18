# posts/utils.py
import requests

def shorten_url(original_url):
    """
    Send link to your URL shortener
    Return shortened URL
    """

    API_URL = "https://dl.jaraflix.com/api/shorten"
    API_KEY = "Tijania32000"

    try:
        response = requests.post(
            API_URL,
            json={
                "url": original_url,
                "api_key": API_KEY
            },
            timeout=10
        )

        data = response.json()

        if response.status_code == 200 and "short_url" in data:
            return data["short_url"]

    except Exception:
        pass

    # If anything fails, keep original link
    return original_url
