import json
import os

class WaterTracker:
    def __init__(self, filename="water_data.json"):
        self.filename = filename

        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.glasses = json.load(file).get("glasses", 0)
        else:
            self.glasses = 0

    def add_glass(self):
        self.glasses += 1
        self.save()

    def get_count(self):
        return self.glasses

    def reset(self):
        self.glasses = 0
        self.save()

    def save(self):
        with open(self.filename, "w") as file:
            json.dump({"glasses": self.glasses}, file)


# Global tracker object
tracker = WaterTracker()

def drink_water():
    tracker.add_glass()

def get_water_count():
    return tracker.get_count()

def reset_water_count():
    tracker.reset()