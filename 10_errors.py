"""
10 - Errors and Exceptions

Catch specific exceptions first, general ones last.
finally always runs, whether or not an error occurred.
Python's error messages are unusually clear - read the LAST line first.
"""

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError as e:
        print(f"Wrong type: {e}")
        return None
    finally:
        print("-- attempt finished --")

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "x"))


# --- Common built-in exceptions ---
# ValueError      - right type, wrong value:  int("abc")
# TypeError       - wrong type:               "5" + 5
# KeyError        - missing dict key:         d["nope"]
# IndexError      - list index out of range:  [1,2][5]
# FileNotFoundError
# ZeroDivisionError
# AttributeError  - object has no such method or property

try:
    value = int("not a number")
except ValueError as e:
    print(f"Conversion failed: {e}")

data = {"name": "Abu"}
try:
    print(data["email"])
except KeyError:
    print("Key not found - use .get() to avoid this")


# --- Catching several at once ---
try:
    result = int("abc")
except (ValueError, TypeError) as e:
    print(f"Bad input: {e}")


# --- The general catch goes LAST ---
try:
    risky = 10 / 0
except ZeroDivisionError:
    print("specific handler ran")
except Exception as e:
    print(f"general handler: {e}")


# --- else runs only if nothing was raised ---
try:
    number = int("42")
except ValueError:
    print("failed")
else:
    print(f"Success: {number}")
finally:
    print("always runs")


# --- Raising your own ---
def set_replies(count: int) -> int:
    if not isinstance(count, int):
        raise TypeError("count must be an integer")
    if count < 0:
        raise ValueError("count cannot be negative")
    return count

try:
    set_replies(-5)
except ValueError as e:
    print(f"Rejected: {e}")


# --- Custom exceptions ---
class ThreadLockedError(Exception):
    """Raised when trying to post in a locked thread."""
    pass


def add_reply(thread: dict, text: str) -> str:
    if thread.get("locked"):
        raise ThreadLockedError(f"'{thread['title']}' is locked")
    return f"Reply added to {thread['title']}"

try:
    print(add_reply({"title": "Rules", "locked": True}, "hello"))
except ThreadLockedError as e:
    print(f"Blocked: {e}")


# --- Do not silence errors ---
# BAD - hides real bugs and makes debugging impossible:
# try:
#     something()
# except:
#     pass

# Better: catch what you expect, log the rest.
def safe_parse(text: str, default=None):
    try:
        return int(text)
    except ValueError:
        print(f"Could not parse '{text}', using default")
        return default

print(safe_parse("42"))
print(safe_parse("abc", default=0))


# --- Practice ---
# 1. Write a function that reads a value from a dict and raises a clear
#    custom error if the key is missing.
# 2. Call it inside a try/except and print a friendly message.
