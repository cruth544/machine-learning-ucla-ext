import random
from random import randint


def flip_coin():
    return 'h' if random.random() < .5 else 't'


def run_experiment(num_flips, num_coins, num_experiments):
    results = []
    head_count_coins = []
    for experiment in range(num_experiments):
        for coin in range(num_coins):
            flips = [flip_coin() for i in range(num_flips)]
            count = float(flips.count('h'))/num_flips
            head_count_coins.append(count)

        results.append({'v1': head_count_coins[0],
                        'v_rand': head_count_coins[randint(0, 999)],
                        'v_min':  min(head_count_coins)})
        head_count_coins = []

    return results
