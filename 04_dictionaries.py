"""
04 - Dictionaries

Key-value pairs - PHP's associative array.
This is the most important structure for API work: every JSON response
you ever handle arrives as a dict.
"""

user = {
    "name": "Abu",
    "role": "developer",
    "years": 7
}

# --- Access ---
print(user["name"])                    # Abu - raises KeyError if missing
print(user.get("email"))               # None - safe, no error
print(user.get("email", "unknown"))    # "unknown" - with a fallback

# Use .get() when a key might be missing.
# Use [...] when it definitely should exist - the error is helpful there.


# --- Adding and updating ---
user["email"] = "abu@example.com"      # add
user["years"] = 8                      # update
user.update({"city": "Sialkot", "active": True})   # several at once
print(user)


# --- Removing ---
del user["active"]
removed = user.pop("city")             # remove and return the value
print(f"Removed: {removed}")


# --- Checking ---
print("name" in user)                  # True - checks KEYS, not values
print("Abu" in user.values())          # True - check values explicitly


# --- Iterating ---
for key in user:                       # loops over keys by default
    print(key)

for key, value in user.items():        # like foreach ($u as $k => $v)
    print(f"{key}: {value}")

for value in user.values():
    print(value)

print(list(user.keys()))


# --- Nesting: this is the shape of JSON ---
forum = {
    "name": "johnnydoe.is",
    "stats": {"threads": 5000, "users": 1200},
    "tags": ["gaming", "trading"],
    "admins": [
        {"name": "Abu", "role": "owner"},
        {"name": "Sara", "role": "mod"}
    ]
}

print(forum["stats"]["threads"])           # 5000
print(forum["tags"][0])                    # gaming
print(forum["admins"][1]["name"])          # Sara

# Safe access through several levels
print(forum.get("stats", {}).get("posts", 0))    # 0 instead of an error


# --- A list of dicts: the most common real-world shape ---
threads = [
    {"title": "Welcome", "replies": 42, "locked": False},
    {"title": "Rules", "replies": 3, "locked": True},
    {"title": "Trading guide", "replies": 128, "locked": False},
]

for t in threads:
    print(f"{t['title']} - {t['replies']} replies")

# Note the quote style: single quotes inside an f-string that uses double.

busy = [t for t in threads if t["replies"] > 10]
print(len(busy))

by_replies = sorted(threads, key=lambda t: t["replies"], reverse=True)
print(by_replies[0]["title"])          # Trading guide

# lambda is a small inline function. The line above means:
# "sort these, using each item's replies value as the sort key"


# --- Practice ---
# 1. Build a dict describing one of your XenForo addons.
# 2. Nest a list of its features inside.
# 3. Loop over a list of three such addons and print each name.
