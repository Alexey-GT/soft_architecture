from Homework_2.ItemFabric import ItemFabric
from Homework_2.GemReward import GemReward


class GemGenerator(ItemFabric):

    def create_item(self):
        print("Created a chest with precious stones")
        return GemReward()