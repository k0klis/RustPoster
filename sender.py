import requests as req
import schedule
from time import sleep
from datetime import datetime
from websocket import create_connection
import json
import random

def send(token, channel_id, message, delay, image):
    channelids = channel_id.split(', ')
    messagebytes = message.encode('utf-8')
    def sendMessage(token, channelid, message, image):
        ws = create_connection("wss://gateway.discord.gg/")
        data = '''
        {
            "op": 2,
            "d":{
                "token": "%s",
                "properties": {
                    "$os": "linux",
                    "$browser": "ubuntu",
                    "$device": "ubuntu"
                },
            }
        }
        ''' % token
        ws.send(data)
        if image != '':
            headers = {'authorization': token}
            files = {'files[0]': open(image, 'rb')}
            files['payload_json'] = (None, json.dumps({'content': message}))
            req.post("https://discordapp.com/api/v9/channels/%s/messages" % channelid, headers = headers, files=files)
        else:
            headers = {'authorization': token, 'Content-Type': 'application/json'}
            payload = {"content":messagebytes.decode('utf-8'), "tts":False}
            req.post("https://discordapp.com/api/v9/channels/%s/messages" % channelid, headers = headers, json=payload)
        try:
            ws.close()
        except:
            pass
        current_datetime = datetime.now()
        print(f"{current_datetime}  |   MSG sended to {channelid}")


    def time():
        for channelid in channelids:
            sendMessage(token, channelid, message, image)

    for channelid in channelids:
            sendMessage(token, channelid, message, image)
    schedule.every(int(delay)).minutes.do(time)

    while True:
        schedule.run_pending()
        sleep(1)
