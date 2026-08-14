class TestBot:
    inventory = []   

    def __init__(self, name):
        self.name = name

    def add_item(self, name):
        self.inventory.append(name)


class TestBot2:
    def __init__(self, name):
        self.name = name
        self.inventory = []   

    def add_item(self, name):
        self.inventory.append(name)


print("--- Buggy version ---")
r1 = TestBot("Bastion")
r2 = TestBot("Orisa")
r1.add_item("wrench")
r2.add_item("battery pack")
print(r1.inventory)
print(r2.inventory)

print("--- Fixed version ---")
r3 = TestBot2("Bastion")
r4 = TestBot2("Orisa")
r3.add_item("wrench")
r4.add_item("battery pack")
print(r3.inventory)
print(r4.inventory)