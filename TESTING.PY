# DISCORD WEBHOOK EXAMPLE
import requests
import time
import json


def POST(content=''):
    # Data
    ENDPOINT_URL = 'https://discord.com/api/webhook/'
    DATA = {
        "avatar_url": 'https://banner2.cleanpng.com/20181110/su/kisspng-discord-social-media-portable-network-graphics-cli-1713924150656.webp',
        "embeds": [
            {
                "title": 'Message',
                "description": content,
                "color": 16711680  # Red color in decimal
            }
        ],
    }

    # Specify the POST request will be a JSON object/JSON formatted
    HEADERS = {
        "Content-Type": "application/json"
    }

    # POST request
    response = requests.post(url=ENDPOINT_URL, data=json.dumps(obj=DATA), headers=HEADERS)
    # Display Request Status Code
    print(response)


while prompt := input('Enter content: '):
    if prompt == ':q!': break
    POST(content=prompt)
    time.sleep(1)