import json
import threading

import requests
from redis import Redis
from rq import Queue


def setInterval(func, time):
    e = threading.Event()
    while not e.wait(time):
        func()


def foo():
    print("hello")


def data_switcher(bundle, driver):
    switcher = {
        "MTN-1GB": '"mat-radio-13"',
        "MTN-2GB": '"mat-radio-14"',
        "MTN-3GB": '"mat-radio-15"',
        "MTN-5GB": '"mat-radio-16"'
    }

    return '//*[@id={data_string}]/label/div[1]'.format(data_string=switcher[bundle])


def sendWebhook(url, data):
    requests.post(url, data=json.dumps(data))

def testQueue():
    q = Queue(connection=Redis())

    result = q.enqueue(sendWebhook,"https://enfx4226l3b9k.x.pipedream.net/")



# sendWebhook("https://enfx4226l3b9k.x.pipedream.net/", {"reference": "sadiqumar18"})


testQueue()