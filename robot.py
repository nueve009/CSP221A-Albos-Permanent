from abc import ABC, abstractmethod

class InsufficientBatteryError(Exception):
    def __init__(self, name, required, available):
        self.name = name
        self.required = required
        self.available = available
        message = f"{name} needs {required}% battery for this task but only has {available}%."
        super().__init__(message)

class Robot(ABC):
    manufacturer = "Omnics"
    population = 0

    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery
        Robot.population += 1  

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self,value):
        self._battery = max(0, min(value, 100))

    def use_battery(self, amount):
        if amount > self.battery:
            raise InsufficientBatteryError(self.name, amount, self.battery)
        self.battery -= amount

    def __str__(self):
        return f"{self.name} currently have {self.battery}% battery remaining."

    def __repr__(self):
        return f"Robot(name={self.name!r}, battery={self.battery})"

    @abstractmethod
    def perform_task(self):
        pass
    
# r1 = Robot("Bastion")
# r2 = Robot("Ramattra", 500)
# r3 = Robot("Orisa", -50)
# r4 = Robot("Zenyatta", 75)

# print(r1)
# print(r2)
# print(r3)
# print(r4)
# print([r1, r2, r3, r4])

# print(Robot.manufacturer)
# print(Robot.population)


class CleaningRobot(Robot):
    def __init__(self, name, battery=5, capacity = 100):
        super().__init__(name, battery)
        self.capacity = capacity

    def perform_task(self):
        self.use_battery -=10
        return f"{self.name} is cleaning. Battery is now at {self.battery}%."

class DroneRobot(Robot):
    def __init__(self, name, battery=100, altitude=0):
        super().__init__(name, battery)
        self.altitude = altitude

    def perform_task(self):
        self.use_battery -=15
        return f"{self.name} is flying at {self.altitude} meters. Battery is now at {self.battery}%."

def fleet_report(robots):
    for robot in robots:
        print(str(robot))

c1 = CleaningRobot("C-Bot")
d1 = DroneRobot("AquaBot")

print(c1.perform_task())
print(c1)

print(d1.perform_task())
print(d1)

fleet = [c1, d1]
fleet_report(fleet)
