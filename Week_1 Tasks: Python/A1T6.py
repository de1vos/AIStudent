# Task 6: Logging and Decorators

## Story:
# You are building a user management system that logs user actions like logging in, 
# updating profiles, and making purchases for regulatory reasons. 
# You want to add a decorator to log the timestamp of each action.

## Tasks:
# - Create a decorator function `log_action` that logs the action name and timestamp.
# - Decorate the `login`, `update_profile`, and `make_purchase` functions 
#   with the `log_action` decorator.
# - Test the decorated functions by calling them with sample arguments.

## Starting Point:

import time
from functools import wraps

# Decorator to log actions
def log_action(action_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = time.gmtime(time.time())
            modified = f"{result.tm_year}-{result.tm_mon:02d}-{result.tm_mday:02d} {result.tm_hour:02d}:{result.tm_min}:{result.tm_sec:02d}"
            log = {
                "Action": action_type,
                "Timestamp": modified
                }
            for key, value in log.items():
                if (key == "Action"):
                    print(f"{key} : {value}", end = ' | ')
                else:
                    print(f"{key} : {value}")

            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_action("Login")
def login(username):
    print(f"{username} logged in successfully.")

@log_action("Profile update")
def update_profile(username, new_email):
    print(f"{username} updated their profile. New email: {new_email}")

@log_action("Purchase")
def make_purchase(username, item):
    print(f"{username} purchased {item}.")

# Test the decorated functions
login("johndoe")
update_profile("johndoe", "john@example.com")
make_purchase("johndoe", "laptop")

## Expected Output:
# Action: login | Timestamp: 2022-01-01 12:00:00
# johndoe logged in successfully.
# Action: update_profile | Timestamp: 2022-01-01 12:00:01
# johndoe updated their profile. New email: john@example.com
# Action: make_purchase | Timestamp: 2022-01-01 12:00:02
# johndoe purchased laptop.