#!/usr/bin/python3
import urllib.request


def fetch_url(url):
    """
    Fetches the content from the provided URL using urllib package.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        bytes: The content retrieved from the URL.
    """
    with urllib.request.urlopen(url) as response:
        return response.read()


if __name__ == "__main__":
    target_url = 'https://alx-intranet.hbtn.io/status'

    body_content = fetch_url(target_url)

    print("Body response:")
    print("\t- type:", type(body_content))
    print("\t- content:", body_content)
    print("\t- utf8 content:", body_content.decode('utf-8'))
