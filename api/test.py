import time

import schedule as schedule


def job():
  print("hello")


while True:
  schedule.run_pending()
  time.sleep(1)



schedule.every(10).seconds.do(job)