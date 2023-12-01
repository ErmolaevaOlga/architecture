from seminar2.fabrics.bronze_generator import BronzeGenerator
from seminar2.fabrics.gold_generator import GoldGenerator
from random import randint

from seminar2.fabrics.silver_generator import SilverGenerator

if __name__ == '__main__':
    rewards = [GoldGenerator(), BronzeGenerator(), SilverGenerator()]

    for i in range(20):
        rewards[randint(0, 1)].create_item().open()