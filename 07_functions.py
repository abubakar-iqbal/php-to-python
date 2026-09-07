"""
07 - Functions

Named arguments and default values are used far more heavily in Python
than in PHP. Every library you will use relies on them.
Type hints are optional but worth adopting from day one.
"""

def greet(name):
    return f"Hello, {name}"

print(greet("Abu"))


# --- Default values ---
def greet_with(name, greeting="Hello"):
    return f"{greeting}, {name}"

print(greet_with("Abu"))
print(greet_with("Abu", "Salam"))


# --- Named arguments: order stops mattering ---
print(greet_with(greeting="Hi", name="Abu"))

# You will see this constantly in real libraries, e.g.
#   client.messages.create(model=..., max_tokens=..., messages=[...])


# --- Type hints ---
def summarize(text: str, max_words: int = 50) -> str:
    """Return the first max_words words of text."""
    words = text.split()
    return " ".join(words[:max_words])

print(summarize("one two three four five", max_words=3))

# Hints document intent and let your editor catch mistakes.
# They are NOT enforced at runtime - passing an int still runs.


# --- Docstrings ---
def calculate_rate(hours: float, rate: float) -> float:
    """
    Calculate total pay.

    Args:
        hours: Hours worked
        rate: Hourly rate

    Returns:
        Total amount owed
    """
    return hours * rate

print(calculate_rate(10, 25.5))
print(calculate_rate.__doc__)


# --- Returning several values ---
def stats(numbers: list) -> tuple:
    return min(numbers), max(numbers), sum(numbers)

low, high, total = stats([3, 7, 2])
print(low, high, total)                 # 2 7 12


# --- Returning a dict when there are many values ---
def analyze(text: str) -> dict:
    words = text.split()
    return {
        "words": len(words),
        "characters": len(text),
        "longest": max(words, key=len) if words else None
    }

result = analyze("the quick brown fox")
print(result["words"], result["longest"])


# --- Variable arguments ---
def total_all(*numbers):
    """*args collects positional arguments into a tuple."""
    return sum(numbers)

print(total_all(1, 2, 3, 4))

def build_config(**options):
    """**kwargs collects named arguments into a dict."""
    return options

print(build_config(host="localhost", port=3306))


# --- The mutable default trap ---
# WRONG - the list is created once and shared between calls:
# def add_item(item, items=[]):
#     items.append(item)
#     return items

# RIGHT:
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("a"))
print(add_item("b"))            # ['b'], not ['a', 'b']


# --- Scope ---
counter = 0

def increment():
    global counter              # needed to modify a module-level variable
    counter += 1

increment()
print(counter)                  # 1

# Prefer returning a value over using global. Global state is hard to debug.


# --- lambda: small inline functions ---
double = lambda x: x * 2
print(double(5))

threads = [{"title": "A", "replies": 5}, {"title": "B", "replies": 20}]
top = sorted(threads, key=lambda t: t["replies"], reverse=True)
print(top[0]["title"])

# Use lambda only for one-liners passed to sorted/filter/map.
# Anything longer deserves a real def.


# --- Practice ---
# 1. Write a function that takes a list of threads and returns only the busy ones.
# 2. Give it a default threshold of 10 replies.
# 3. Add type hints and a docstring.
