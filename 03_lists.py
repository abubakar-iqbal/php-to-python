"""
03 - Lists

A list is PHP's indexed array. Ordered, changeable, allows duplicates.
Watch the difference between sorted(x) and x.sort() - a classic bug source.
"""

skills = ["php", "laravel", "mysql"]

# --- Access ---
print(skills[0])          # php
print(skills[-1])         # mysql   last item
print(len(skills))        # 3
print(skills[0:2])        # ['php', 'laravel']  end excluded


# --- Adding ---
skills.append("python")            # add to end
skills.insert(1, "xenforo")        # insert at position 1
skills.extend(["redis", "docker"]) # add several at once
print(skills)


# --- Removing ---
skills.remove("mysql")             # remove by value (first match)
last = skills.pop()                # remove and return last item
second = skills.pop(1)             # remove and return by index
print(f"Removed: {last}, {second}")
print(skills)


# --- Searching ---
print("php" in skills)             # True - membership check
print(skills.index("laravel"))     # position of a value
print(skills.count("php"))         # how many times it appears


# --- Sorting: the important distinction ---
nums = [5, 2, 9, 1]

new_list = sorted(nums)            # returns a NEW list, original untouched
print(new_list)                    # [1, 2, 5, 9]
print(nums)                        # [5, 2, 9, 1] - unchanged

nums.sort()                        # sorts IN PLACE, returns None
print(nums)                        # [1, 2, 5, 9]

# This is the bug to avoid:
# result = nums.sort()   -> result is None, not a list

nums.sort(reverse=True)
print(nums)                        # [9, 5, 2, 1]

words = ["banana", "Apple", "cherry"]
print(sorted(words, key=str.lower))   # case-insensitive sort


# --- Numbers ---
values = [3, 7, 2, 8]
print(sum(values), min(values), max(values))
print(sum(values) / len(values))      # average


# --- Copying: this trips people up ---
original = [1, 2, 3]
wrong = original                      # both names point to the SAME list
wrong.append(4)
print(original)                       # [1, 2, 3, 4] - original changed too

right = original.copy()               # a real copy
right.append(5)
print(original)                       # unchanged


# --- Tuples: like lists, but immutable ---
point = (10, 20)
print(point[0])
# point[0] = 5   -> TypeError, cannot change a tuple

# Useful for returning several values from a function
low, high = (1, 100)
print(low, high)


# --- Sets: unique values, no order ---
tags = {"php", "python", "php"}
print(tags)                           # {'php', 'python'} - duplicate dropped
print(len(set([1, 2, 2, 3])))         # 3 - quick way to count unique items


# --- Practice ---
# 1. Build a list of five forum thread titles.
# 2. Sort them alphabetically without changing the original.
# 3. Print only the titles longer than 10 characters.
