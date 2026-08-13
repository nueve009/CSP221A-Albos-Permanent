class Robot:
    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self,value):
        self._battery = max(0, min(value, 100))
    
r1 = Robot("bastion")
r2 = Robot("Ramattra", 500)

print(r1.name, r1.battery)
print(r2.name, r2.battery)