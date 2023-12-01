from seminar2.fabrics.bronze_generator import BronzeGenerator
from seminar2.fabrics.gem_generator import GemGenerator
from seminar2.fabrics.gold_generator import GoldGenerator
from random import randint

from seminar2.fabrics.silver_generator import SilverGenerator
from seminar2.fabrics.wood_generator import WoodGenerator

if __name__ == '__main__':
    rewards = [GoldGenerator(), BronzeGenerator(), SilverGenerator(), WoodGenerator(), GemGenerator()]

    for i in range(20):
        rewards[randint(0, 4)].create_item().open()