from Homework_2.ItemFabric import ItemFabric
from Homework_2.SilverReward import SilverReward


class SilverGenerator(ItemFabric):

    def create_item(self):
        print("Created a chest with silver")
        return SilverReward()
