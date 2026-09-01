"""
01 - Variables and Types

Coming from PHP: no $, no semicolons, no type declaration.
The big difference: PHP quietly converts types for you ("25" + 5 works).
Python refuses and raises TypeError. That catches bugs early.
"""

# --- Basic types ---
name = "Abu"          # str
count = 7             # int
price = 99.5          # float
active = True         # bool - capitalized, unlike PHP's true
nothing = None        # PHP's null

print(name, count, price, active, nothing)

# type() tells you what something is - useful when debugging
print(type(name))     # <class 'str'>
print(type(count))    # <class 'int'>


# --- Type conversion is explicit ---
age_text = "25"
age = int(age_text)
print(age + 5)                    # 30

n = 7
print("Count: " + str(n))         # must convert; Python won't mix str and int
print(float("3.14"))              # 3.14
print(int(9.99))                  # 9 - truncates, does not round
print(round(9.99))                # 10


# --- Multiple assignment ---
a, b, c = 1, 2, 3
print(a, b, c)

x = y = 0                         # both set to 0
print(x, y)

# Swapping without a temp variable
a, b = b, a
print(a, b)


# --- Constants are a convention, not enforced ---
# UPPERCASE means "do not change this" - Python will not stop you
MAX_RETRIES = 3
API_TIMEOUT = 30


# --- Checking types ---
value = "hello"
print(isinstance(value, str))     # True
print(isinstance(count, int))     # True


# --- Practice ---
# 1. Create a variable for your forum name and thread count.
# 2. Print a sentence using both.
# 3. Try "5" + 5 and read the error message carefully.
