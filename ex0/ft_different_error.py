#!/usr/bin/env python3

import sys

def send_help() -> None:
    total_arg = len(sys.argv)
    if total_arg <= 1:
        print("No arguments provided!")
        print(f"Total arguments: {total_arg}\n")
        return
    print(f"Arguments received: {total_arg-1}")
    for i in range(1, total_arg):
        print(f"Argument: {sys.argv[i]}")
    print(f"Total arguments: {total_arg}\n")
    

if __name__ == "__main__":
    print("=== Command Quest ===")
    print("Program name: ft_command_quest.py")
    send_help()
