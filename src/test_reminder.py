from reminder import Reminder

# 10 seconds for testing
reminder = Reminder(interval_minutes=10/60)

print("Reminder started...")
reminder.start()

input("Press Enter to stop...\n")
reminder.stop()