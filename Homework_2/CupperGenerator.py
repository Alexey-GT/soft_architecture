from Homework_2.ItemFabric import ItemFabric
from Homework_2.CupperReward import CupperReward


class CupperGenerator(ItemFabric):

    def create_item(self):
        print("Create cupper")
        return CupperReward()