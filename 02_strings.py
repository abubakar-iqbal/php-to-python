"""
02 - Strings

f-strings replace PHP's string interpolation and concatenation.
String methods chain left to right: text.strip().lower()
"""

name = "Abu"
project = "johnnydoe.is"

# --- f-strings: use these, not concatenation ---
print(f"{name} runs {project}")
print(f"Total: {5 * 3}")                  # expressions work inside braces
print(f"Upper: {name.upper()}")           # method calls work too

# Number formatting inside f-strings
price = 1234.5678
print(f"{price:.2f}")                     # 1234.57 - two decimals
print(f"{price:,.2f}")                    # 1,234.57 - thousands separator


# --- Common methods ---
text = "  Hello World  "
print(text.strip())                       # removes surrounding whitespace
print(text.strip().lower())               # hello world
print(text.strip().upper())               # HELLO WORLD
print(text.strip().title())               # Hello World

print("hello".replace("l", "L"))          # heLLo
print(len("hello"))                       # 5
print("hello".startswith("he"))           # True
print("hello".endswith("lo"))             # True
print("world" in "hello world")           # True - substring check
print("Hello".count("l"))                 # 2


# --- split and join are opposites ---
csv_line = "php,laravel,python"
parts = csv_line.split(",")
print(parts)                              # ['php', 'laravel', 'python']

rejoined = "-".join(parts)
print(rejoined)                           # php-laravel-python

sentence = "the quick brown fox"
words = sentence.split()                  # no argument = split on whitespace
print(words)
print(len(words))                         # 4 - handy word counter


# --- Slicing: start included, end excluded ---
s = "development"
print(s[0])          # d
print(s[-1])         # t      negative counts from the end
print(s[0:5])        # devel  indexes 0,1,2,3,4
print(s[:5])         # devel  from the beginning
print(s[5:])         # opment to the end
print(s[-3:])        # ent    last three characters
print(s[::-1])       # tnempoleved - reversed


# --- Multi-line strings ---
message = """Dear member,

Your thread has been approved.
"""
print(message)


# --- Checking content ---
print("abc123".isalnum())      # True
print("abc".isalpha())         # True
print("123".isdigit())         # True - useful for validating input


# --- Practice ---
# 1. Take "  PHP, Laravel, MySQL  " and produce a clean lowercase list.
# 2. Write a function-free snippet that counts words in a sentence.
