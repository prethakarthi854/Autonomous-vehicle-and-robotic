import random
import time

class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.speed = 0  # in km/h

    def update_speed(self):
        # Simulate speed update between 0 and 150 km/h
        self.speed = random.randint(0, 150)

    def get_speed(self):
        return self.speed

class AutonomousSystem:
    def __init__(self, num_vehicles):
        self.vehicles = [Vehicle(i) for i in range(1, num_vehicles + 1)]

    def detect_vehicles(self):
        # Simulate detection and speed reading
        for vehicle in self.vehicles:
            vehicle.update_speed()

    def display_speeds(self):
        print("Detected vehicle speeds:")
        for vehicle in self.vehicles:
            print(f"Vehicle {vehicle.vehicle_id}: {vehicle.get_speed()} km/h")

# Example usage
if __name__ == "__main__":
    auto_system = AutonomousSystem(num_vehicles=5)

    while True:
        auto_system.detect_vehicles()
        auto_system.display_speeds()
        print("-" * 30)
        time.sleep(2)  # Simulate time between scans
