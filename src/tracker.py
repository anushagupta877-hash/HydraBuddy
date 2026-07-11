class WaterTracker:
    def __init__(self):
        self.glasses = 0

    def add_glass(self):
        self.glasses += 1

    def get_count(self):
        return self.glasses

    def reset(self):
        self.glasses = 0