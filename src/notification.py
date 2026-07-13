from plyer import notification

def show_notification():
    notification.notify(
        title="💧 Water Reminder",
        message="Time to drink a glass of water!",
        app_name="HydraBuddy",
        timeout=10
    )