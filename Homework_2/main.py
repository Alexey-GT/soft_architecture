import random

from Homework_2.GemGenerator import GemGenerator
from Homework_2.GoldGenerator import GoldGenerator
from Homework_2.SilverGenerator import SilverGenerator
from Homework_2.CupperGenerator import CupperGenerator

if __name__ == '__main__':
    fabricList = [GemGenerator(), GoldGenerator(), SilverGenerator(), CupperGenerator()]
    for i in range(20):
        rnd = random.choice(fabricList).create_item().open()
