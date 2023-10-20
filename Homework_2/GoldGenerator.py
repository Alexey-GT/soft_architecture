from Homework_2.ItemFabric import ItemFabric
from Homework_2.GoldReward import GoldReward


class GoldGenerator(ItemFabric):

    def create_item(self):
        print("Created a chest of gold")
        return GoldReward()