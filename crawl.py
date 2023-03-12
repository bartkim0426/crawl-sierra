import os
from datetime import datetime

import httpx
from bs4 import BeautifulSoup

SLACK_HOOK_URL = os.environ.get('SLACK_HOOK_URL')


def send_slack_message(message):
    message = {'text': message}
    httpx.post(SLACK_HOOK_URL, json=message, headers={'Content-Type': 'application/json'})


def crawl_sierra():
    url = 'https://www.sierra.com/five-ten-hiangle-pro-climbing-shoes-for-men~p~83yhm/'
    res = httpx.get(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    })
    html_doc = res.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    select = soup.find_all('select')[1]
    options = select.find_all('option')
    values = []
    for option in options:
        try:
            value = float(option.text)
            values.append(value)
        except ValueError:
            pass

    largest_size = max(values)
    print(f'largest_size: {largest_size}')

    if largest_size in [7, 8.5]:
        message = f'''new size in hiangle: {largest_size}
        {url}
        '''
        send_slack_message(message)

def crawl_sierra_crawe():
    url = 'https://www.sierra.com/five-ten-crawe-climbing-shoes-for-women~p~83yhk/'
    res = httpx.get(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    })
    html_doc = res.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    select = soup.find_all('select')[1]
    options = select.find_all('option')
    values = []
    for option in options:
        try:
            value = float(option.text)
            values.append(value)
        except ValueError:
            pass

    size = 8
    if size in values:
        message = f'{size} size in crawe: {url}'
        send_slack_message(message)


if __name__ == '__main__':
    print(f'executed: {datetime.now()}')
    crawl_sierra()
