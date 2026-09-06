"""
06 - Loops

There is no C-style for loop with a counter in Python.
You loop over the collection directly.
"""

skills = ["php", "laravel", "python"]

# --- Basic loop ---
for skill in skills:
    print(skill)


# --- Need the index too? ---
for i, skill in enumerate(skills):
    print(i, skill)                    # 0 php, 1 laravel, 2 python

for i, skill in enumerate(skills, start=1):
    print(f"{i}. {skill}")             # 1. php, 2. laravel ...


# --- Looping a dict ---
user = {"name": "Abu", "role": "developer"}

for key, value in user.items():
    print(f"{key}: {value}")


# --- A fixed number of times ---
for i in range(5):                     # 0,1,2,3,4 - end excluded
    print(i)

for i in range(1, 6):                  # 1,2,3,4,5
    print(i)

for i in range(0, 10, 2):              # 0,2,4,6,8 - step of 2
    print(i)

for i in range(5, 0, -1):              # 5,4,3,2,1 - counting down
    print(i)


# --- while ---
count = 0
while count < 3:
    print(count)
    count += 1                         # there is no ++ in Python


# --- break and continue ---
for n in range(10):
    if n == 3:
        continue                       # skip this iteration
    if n == 6:
        break                          # exit the loop entirely
    print(n)                           # 0,1,2,4,5


# --- Two lists at once ---
names = ["Abu", "Sara"]
roles = ["owner", "mod"]

for name, role in zip(names, roles):
    print(f"{name} is {role}")


# --- Nested loops ---
forums = ["gaming", "trading"]
sections = ["news", "help"]

for forum in forums:
    for section in sections:
        print(f"{forum}/{section}")


# --- Accumulating results ---
threads = [
    {"title": "Welcome", "replies": 42},
    {"title": "Rules", "replies": 3},
    {"title": "Guide", "replies": 128},
]

total = 0
busiest = None

for t in threads:
    total += t["replies"]
    if busiest is None or t["replies"] > busiest["replies"]:
        busiest = t

print(f"Total replies: {total}")
print(f"Busiest: {busiest['title']}")


# --- Modifying a list while looping over it: don't ---
# Loop over a copy instead, or build a new list.
nums = [1, 2, 3, 4, 5]
kept = [n for n in nums if n % 2 == 0]     # build new, do not mutate
print(kept)


# --- Practice ---
# 1. Loop over your skills list and print each with its position.
# 2. Sum the replies of only the threads with more than 10 replies.
# 3. Print a 3x3 grid of coordinates using nested loops.
