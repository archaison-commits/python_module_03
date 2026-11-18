#!/usr/bin/env python3

import sys

def ft_score_analytics() -> None:
    if len(sys.argv) <= 1:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    valid_scores = []
    valid_players: int = 0
    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            valid_scores.append(score)
            valid_players += 1
        except ValueError:
            print(f"Invalid parameter '{arg}'")
    if not valid_scores:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    if valid_players > 0:
        total_score = sum(valid_scores)
        avg_score = total_score / valid_players
        high_score = max(valid_scores)
        low_score = min(valid_scores)
        score_range = high_score - low_score
        print(f"Scores processed: {valid_scores}")
        print(f"Total players: {valid_players}")
        print(f"Total Score: {total_score}")
        print(f"Average Score: {avg_score}")
        print(f"Heigh Score: {high_score}")
        print(f"Low Score: {low_score}")
        print(f"Score range: {score_range}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
    print()
