#!/usr/bin/env python3

import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    total_players = [
        "Alice", "bob", "Charlie",
        "dylan", "Emma", "Gregory",
        "john", "kevin", "Liam"]
    cap_players = [player.capitalize() for player in total_players]
    ini_cap_players = [
        player for player in total_players if player == player.capitalize()]
    dic_cap_players = {
        player: random.randint(1, 1000) for player in cap_players}
    average_score = sum(dic_cap_players.values()) / len(dic_cap_players)
    high_scores = {
        player: score for player, score in dic_cap_players.items()
        if score > average_score}
    print(f"Initial list of players: {total_players}")
    print(f"New list with all names capitalized: {cap_players}")
    print(f"New list of capitalized names only: {ini_cap_players}")
    print(f"Score dict: {dic_cap_players}")
    print(f"Score average is {round(average_score, 2)}")
    print(f"High scores: {high_scores}")
