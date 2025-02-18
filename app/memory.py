import json
import os

class Memory:
    """Manages farmer’s activities and stores them in a JSON file."""
    
    def __init__(self, memory_file="farmer_memory.json"):
        self.memory_file = memory_file
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as f:
                return json.load(f)
        return {}

    def save_memory(self):
        with open(self.memory_file, "w") as f:
            json.dump(self.memory, f, indent=4)

    def add_activity(self, farmer_id, activity):
        if farmer_id not in self.memory:
            self.memory[farmer_id] = []
        if activity not in self.memory[farmer_id]:
            self.memory[farmer_id].append(activity)
            self.save_memory()

    def get_activities(self, farmer_id):
        return self.memory.get(farmer_id, [])
