class TV:
    def __init__(self):
        self.on=False
        self.color="Black"
    
    def turnOn(self):
        self.on=True
        print("TurnOn called!!!")