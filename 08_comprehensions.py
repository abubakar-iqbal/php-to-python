"""
08 - Comprehensions

You will see these everywhere in Python code, so learn to READ them
even before you are comfortable writing them.

Read as: [ expression   for item in collection   if condition ]
              what           the loop              the filter
"""

skills = ["php", "laravel", "python", "redis"]

# --- The long way ---
upper = []
for s in skills:
    upper.append(s.upper())
print(upper)

# --- The Python way ---
upper = [s.upper() for s in skills]
print(upper)


# --- With a filter ---
long_ones = [s for s in skills if len(s) > 4]
print(long_ones)                          # ['laravel', 'python', 'redis']


# --- Transform and filter together ---
result = [s.upper() for s in skills if s.startswith("p")]
print(result)                             # ['PHP', 'PYTHON']


# --- Numbers ---
squares = [n * n for n in range(1, 6)]
print(squares)                            # [1, 4, 9, 16, 25]

evens = [n for n in range(20) if n % 2 == 0]
print(evens)


# --- On a list of dicts: the realistic case ---
threads = [
    {"title": "Welcome", "replies": 42, "locked": False},
    {"title": "Rules", "replies": 3, "locked": True},
    {"title": "Trading guide", "replies": 128, "locked": False},
]

titles = [t["title"] for t in threads]
print(titles)

busy = [t for t in threads if t["replies"] > 10]
print(len(busy))

open_titles = [t["title"] for t in threads if not t["locked"]]
print(open_titles)

total = sum(t["replies"] for t in threads)     # no brackets needed inside sum
print(total)


# --- Dict comprehension ---
lengths = {s: len(s) for s in skills}
print(lengths)                            # {'php': 3, 'laravel': 7, ...}

lookup = {t["title"]: t["replies"] for t in threads}
print(lookup["Rules"])                    # 3


# --- Set comprehension: unique values ---
first_letters = {s[0] for s in skills}
print(first_letters)                      # {'p', 'l', 'r'}


# --- Conditional expression inside ---
labels = ["hot" if t["replies"] > 10 else "quiet" for t in threads]
print(labels)

# Note the position: when you transform, the if/else goes BEFORE the for.
# When you filter, the if goes AFTER the for.


# --- Nested, but keep it readable ---
pairs = [(f, s) for f in ["gaming", "trading"] for s in ["news", "help"]]
print(pairs)

# If a comprehension needs more than one line to understand,
# write a normal loop instead. Clever is not the goal.


# --- Practice ---
# 1. From the threads list, build a list of titles in uppercase.
# 2. Build a dict mapping title -> locked status.
# 3. Count how many threads have more than 5 replies, in one line.
