from sender import *
import sys
import json


def run():
    try:
        with open('data.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            token = data['token']
            channel_id = data['channelid']
            delay = data['delay']
            image = data['image']
            message = data['message']
            send(token, channel_id, message, delay, image)

    except Exception as e: 
        print(e)
        pass

run()