#!/usr/bin/env python3

import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "charlie", "bob", "dylan"]
    actions = [
        "run", "sleep", "grab", "move",
        "climb", "swim", "use", "release",
        ]
    while True:
        selected_event = (random.choice(players), random.choice(actions))
        yield selected_event


def consume_event(
        list_events: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while list_events:
        index = random.randint(0, len(list_events) - 1)
        selected_event = list_events[index]
        list_events[:] = list_events[:index] + list_events[index + 1:]
        yield selected_event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    generator = gen_event()
    for i in range(1000):
        event = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    list_ten_events = []
    for _ in range(10):
        item = next(generator)
        list_ten_events.append(item)
    print(f"Built a list of 10 events: {list_ten_events}")
    for event in consume_event(list_ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_ten_events}")
