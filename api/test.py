import json
import time

import requests
import schedule as schedule

data = {
  "hello": "hi"
}


def job():
  print("hello")


# while True:
#   schedule.run_pending()
#   time.sleep(1)
#
# schedule.every(10).seconds.do(job)


def send_webhook(url, data):
  print("hello")
  requests.post(url, data=json.dumps(data))


send_webhook("https://enfx4226l3b9k.x.pipedream.net/", data)
job()