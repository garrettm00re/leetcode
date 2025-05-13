# https://leetcode.com/problems/find-the-number-of-winning-players/
# two different approaches to the same problem + testing
# 
import numpy as np
import random
import time
import pandas as pd
import tools
from collections import defaultdict

# Approach 1: Tuple Tracking
def approach_1(n, pick):
    players = [[defaultdict(int), 0] for _ in range(n)]
    winners = set()
    for player, color in pick:
        playerTup = players[player]
        playerTup[0][color] += 1
        playerTup[1] = max(playerTup[1], playerTup[0][color])
        if playerTup[1] > player:
            winners.add(player)
    return len(winners)

# Approach 2: Post-Processing Scan
def approach_2(n, pick):
    players = [defaultdict(int) for _ in range(n)]
    for player, color in pick:
        players[player][color] += 1
    
    total = 0
    for idx, player in enumerate(players):
        for score in player.values():
            if score > idx:
                total += 1
                break
    return total

random.seed(42)  # for reproducibility
np.random.seed(42)

n = 10_000
num_picks = 1_000_000  # more data to smooth noise
color_counts = list(range(1, 201, 5))
num_trials = 5  # repeat each test and average

results = []

for num_colors in color_counts:
    times_1 = []
    times_2 = []

    for _ in range(num_trials):
        # Fix the randomness: same seed each trial for fair comparison
        print(f"Running trial {_ + 1} of {num_trials} for {num_colors} unique colors")
        random.seed(42)
        pick = [(random.randint(0, n - 1), random.randint(0, num_colors - 1)) for _ in range(num_picks)]

        print("Running approach 1")
        start_1 = time.time()
        _ = approach_1(n, pick)
        times_1.append(time.time() - start_1)

        print("Running approach 2")
        start_2 = time.time()
        _ = approach_2(n, pick)
        times_2.append(time.time() - start_2)

    avg_time_1 = sum(times_1) / num_trials
    avg_time_2 = sum(times_2) / num_trials
    results.append((num_colors, avg_time_1, avg_time_2))

df = pd.DataFrame(results, columns=["Unique Colors", "Tuple Tracking (s)", "Post-Scan (s)"])
tools.display_dataframe_to_user(name="Smoothed Performance Data", dataframe=df)
