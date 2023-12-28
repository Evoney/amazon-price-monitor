"""Main module

This is a module to run the job.
"""
import time
from os import system
import schedule
from extractor import extractor

extractor()

def job():
    """
    Run Job.
    """
    system("python amazon_tracker.py")

schedule.every(1).hours.do(job)

print('\nWaiting for price drops...')

while True:
    schedule.run_pending()
    time.sleep(1)
