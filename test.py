import json
import threading
import time

import requests
from apscheduler.schedulers.background import BackgroundScheduler

data = {
  "hello": "hi"
}


def someJob():
  print("Every 10 seconds")


# sched = BackgroundScheduler
#
#
# job = sched.add_job(someJob, 'interval', minutes=1)
# job.remove()


def job():
  print("hello")


def printit():
  print("hello")
  t = threading.Timer(5.0, printit)
  # t.daemon = True
  t.start()


from time import time, sleep

while True:
  sleep(60 - time() % 60)
  print("hello")

# while True:
#   schedule.run_pending()
#   time.sleep(1)
#
# schedule.every(10).seconds.do(job)


def send_webhook(url, data):
  print("hello")
  requests.post(url, data=json.dumps(data))


# //send_webhook("https://enfx4226l3b9k.x.pipedream.net/", data)
# //job()

def setInterval(func, minutes):
  e = threading.Event()
  while not e.wait(minutes):
    func()


setInterval(job,1)
