class MultiReflexAgent:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp
    def precept(self, room_temps):
        self.room_temps = room_temps
    def actuator(self):
        actions = {}
        for room, temp in self.room_temps.items():
            if temp > self.desired_temp:
                actions[room] = "Turn off the heater."
            else:
                actions[room] = "Turn on the heater."
        return actions

agent = MultiReflexAgent(22)
rooms = {
    "Living Room": 28,
    "Bedroom": 18,
    "Kitchen": 32
}
agent.precept(rooms)
actions = agent.actuator()

for room, action in actions.items():
    print(f"{room}: {action}")
