#!/usr/bin/env python3

import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    amount = random.randint(5, len(achievements))
    player = set(random.sample(achievements, amount))
    return player


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    achievements = [
        "Crafting Genius", "Strategist", "World Savior", "Speed runner",
        "Survivor", "Master Explorer", "Treasure Hunter",
        "Unstoppable", "First Steps", "Collector Supreme", "Untouchable",
        "Sharp Mind", "Boss Slayer"]
    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)
    set_achievements = set(achievements)
    all_achievement = alice.union(bob).union(charlie).union(dylan)
    common_achievement = (
        alice.intersection(bob)
        .intersection(charlie)
        .intersection(dylan))
    alice_dif = alice.difference(bob).difference(charlie).difference(dylan)
    bob_dif = bob.difference(alice).difference(charlie).difference(dylan)
    charlie_dif = charlie.difference(bob).difference(alice).difference(dylan)
    dylan_dif = dylan.difference(bob).difference(charlie).difference(alice)
    alice_missing = set_achievements.difference(alice)
    bob_missing = set_achievements.difference(bob)
    charlie_missing = set_achievements.difference(charlie)
    dylan_missing = set_achievements.difference(dylan)
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")
    print(f"All distinct achievements: {all_achievement}\n")
    print(f"Common achievements: {common_achievement}\n")
    print(f"Only Alice has: {alice_dif}")
    print(f"Only Bob has: {bob_dif}")
    print(f"Only Charlie has: {charlie_dif}")
    print(f"Only Dylan has: {dylan_dif}\n")
    print(f"Alice is missing: {alice_missing}")
    print(f"Bob is missing: {bob_missing}")
    print(f"Charlie is missing: {charlie_missing}")
    print(f"Dylan is missing: {dylan_missing}\n")
