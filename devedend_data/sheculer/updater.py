
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from devedend_data import task

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(task.change_data, 'interval', minutes=10)
    print("Starting....")
    scheduler.start()
    print(scheduler.print_jobs())
