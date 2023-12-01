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
        return {
            'type': type(response.read()),
            'content': response.read(),
            'utf8 content': response.read().decode('utf-8')
        }


if __name__ == "__main__":
    target_url = 'https://alx-intranet.hbtn.io/status'

    response_data = fetch_url(target_url)

    print("Body response:")
    print("\t- type:", response_data.get('type'))
    print("\t- content:", response_data.get('content'))
    print("\t- utf8 content:", response_data.get('utf8 content'))
