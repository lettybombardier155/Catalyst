
#### main.py

```python
#!/usr/bin/env python3
import random

messages = [
    "Believe in yourself and all that you are.",
    "Every day is a new beginning.",
    "Success is not final; failure is not fatal.",
    "Your only limit is your mind.",
    "Stay positive, work hard, and make it happen."
]

def get_random_message():
    return random.choice(messages)

def main():
    print("Welcome to the Catalyst Project!")
    print("Here's your motivational message for the day:")
    print(get_random_message())

if __name__ == "__main__":
    main()
