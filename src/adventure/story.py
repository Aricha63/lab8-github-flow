from adventure.utils import read_events_from_file
import random
from rich import print
from rich.console import Console

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[i]You stand still, unsure what to do. The forest swallows you.[/i]"

def left_path(event):
    return "[i]You walk [blue]left[/blue]. " + event + "[/i]"

def right_path(event):
    return "[i]You walk [red]right[/red]. " + event + "[/i]"

if __name__ == "__main__":
    console = Console()
    events = read_events_from_file('events.txt')

    print("[i]You wake up in a dark forest. You can go [b blue]left[/b blue] or [b red]right[/b red][/i].")
    while True:
        choice = console.input("Which direction do you choose? ([b blue]left[/b blue]/[b red]right[/b red]/[b purple]exit[/b purple]): ")
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        print(step(choice, events))
