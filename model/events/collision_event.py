class CollisionEvent:

    def __init__(self,message):
        self.beaten = str(message['beaten'])
        self.beat = str(message['beat'])
        self.attack = message['attack']
        self.state = message['state']

    def __str__(self):
        return "beaten: "+self.beaten+"\nbeat: "+self.beat+"\nattack: "+str(self.attack)+"\nstate: "+str(self.state)