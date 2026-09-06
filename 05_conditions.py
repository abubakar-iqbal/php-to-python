"""
05 - Conditions

The colon and indentation replace PHP's braces.
Indentation IS the syntax - four spaces, consistently.
This is the single biggest adjustment coming from PHP.
"""

count = 7

if count > 10:
    print("high")
elif count > 5:
    print("medium")
else:
    print("low")


# --- Logical operators are words, not symbols ---
active = True

if active and count > 3:
    print("active and busy")

if not active or count == 0:
    print("inactive")

# PHP: && || !
# Python: and or not


# --- Comparison chaining works naturally ---
if 1 <= count <= 10:
    print("in range")          # no need for count >= 1 and count <= 10


# --- Falsy values ---
# These are all treated as False:
#   False, None, 0, 0.0, "" (empty string), [] (empty list), {} (empty dict)

items = []
if not items:
    print("list is empty")     # this runs

name = ""
if not name:
    print("no name given")

# Careful: 0 is falsy. If 0 is a valid value, test explicitly.
replies = 0
if replies == 0:
    print("no replies yet")    # correct
if not replies:
    print("this also runs - may not be what you want")


# --- Use "is" for None, not "==" ---
value = None
if value is None:
    print("no value")

if value is not None:
    print("has a value")


# --- Ternary: value if condition else value ---
status = "active" if active else "inactive"
print(status)

label = f"{count} thread" if count == 1 else f"{count} threads"
print(label)


# --- match: Python's switch (3.10+) ---
role = "admin"

match role:
    case "admin":
        print("full access")
    case "mod":
        print("limited access")
    case "member" | "guest":          # multiple values with |
        print("read only")
    case _:                            # default
        print("unknown role")


# --- Guard clauses keep code flat ---
def process_thread(thread):
    if thread is None:
        return "no thread"
    if thread.get("locked"):
        return "thread is locked"
    if thread.get("replies", 0) == 0:
        return "nothing to process"
    return f"processing {thread['title']}"

print(process_thread({"title": "Welcome", "replies": 5}))
print(process_thread({"title": "Rules", "locked": True}))
print(process_thread(None))


# --- Practice ---
# 1. Write a check that classifies a thread as hot, normal, or quiet by replies.
# 2. Handle the case where the replies key is missing entirely.
