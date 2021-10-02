from apscheduler.schedulers.background import BackgroundScheduler

from jadavjobs_admin.classes import Worker


def worker():
    path = "D:\\PROJECTS\\Python Projects\\Api Tools\\chromedriver.exe"
    url = "https://www.freejobalert.com/"
    worker = Worker(path=path, url=url)
    worker.start_application()
    worker.quit()
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(worker, 'interval', minutes=15)
    scheduler.start()
