import schedule
import time
from os import system
from extractor import extractor

extractor()

def job():
    system("python amazon_tracker.py")

schedule.every(1).hours.do(job)

print('\nWaiting for price drops...')

while True:
    schedule.run_pending()
    time.sleep(1)