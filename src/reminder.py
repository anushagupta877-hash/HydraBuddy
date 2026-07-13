import threading
import time
from gui import show_reminder
class Reminder:
    def __init__(self, interval_minutes=0.05):
        self.interval = interval_minutes * 60
        self.running = False

    def start(self):
        self.running = True
        threading.Thread(target=self._run, daemon=True).start()

    def stop(self):
        self.running = False

    def _run(self):
        while self.running:
            time.sleep(self.interval)
            show_reminder()
            # Global reminder object
reminder = Reminder(interval_minutes=0.05)

def start_reminder():
    reminder.start()

def stop_reminder():
    reminder.stop()