#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        arg = input("Enter new coordinates as float in format 'x,y,z':")
        parts = arg.split(",")
        arg_counter: int = 0
        for i in parts:
            arg_counter += 1
        if arg_counter == 3:
            try:
                coordinates = []
                for val in arg.split(","):
                    arg_checker = val.strip()
                    coordinates.append(float(arg_checker))
                x, y, z = coordinates
                return x, y, z
            except ValueError as e:
                print(f"Error on parameter '{arg_checker}': {e}")
                continue
        else:
            print("Invalid Syntax")
            continue


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_set = get_player_pos()
    x1, y1, z1 = first_set
    print(f"Got a first tuple: {first_set}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    center = round(math.sqrt((x1)**2 + (y1)**2 + (z1)**2), 4)
    print(f"Distances to center {center}\n")
    print("Get a second set of coordinates")
    second_set = get_player_pos()
    x2, y2, z2 = second_set
    distance_2p = round(
        math.sqrt(
            (x2 - x1)**2 +
            (y2 - y1)**2 +
            (z2 - z1)**2), 4)
    print(f"Distance between the 2 sets of coordinates: {distance_2p}")
