
#### main.py

```python
#!/usr/bin/env python3
import random

citadels = [
    "The Crimson Keep – A fortress that once housed the greatest warriors, now reduced to ruins after the last great siege.",
    "The Sunken Bastion – A mighty citadel swallowed by the sea after a mysterious cataclysm.",
    "The Frozen Spire – A tower built in the highest peaks, lost to time beneath eternal snow.",
    "The Obsidian Hold – A city of black stone, abandoned after its people vanished overnight.",
    "The Hollow Crown – A kingdom's last refuge, where the final king ruled alone before fading into legend."
]

def get_random_citadel():
    return random.choice(citadels)

def main():
    print("Welcome to Forgotten Citadels!")
    print("Here is a randomly generated lost stronghold and its history:")
    print(get_random_citadel())

if __name__ == "__main__":
    main()
