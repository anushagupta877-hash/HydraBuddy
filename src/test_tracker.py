from tracker import WaterTracker

tracker = WaterTracker()

print("Current glasses:", tracker.get_count())

tracker.add_glass()

print("After drinking:", tracker.get_count())