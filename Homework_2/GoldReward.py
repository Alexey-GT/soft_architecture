from Homework_2.IGameItem import IGameItem

class GoldReward(IGameItem):
    def open(self):
        print("Opened the chest with gold")