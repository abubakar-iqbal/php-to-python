"""
09 - Classes

__init__ is the constructor.
self is your $this - but it is EXPLICIT: the first parameter of every
method, and you write self.name to reach properties.
There is no public/private keyword.
"""

class Forum:
    def __init__(self, name: str, threads: int = 0):
        self.name = name
        self.threads = threads

    def describe(self) -> str:
        return f"{self.name} has {self.threads} threads"

    def add_thread(self) -> None:
        self.threads += 1


f = Forum("johnnydoe.is", 5000)
print(f.describe())
f.add_thread()
print(f.threads)                  # 5001


# --- Class attributes vs instance attributes ---
class Config:
    version = "1.0"               # shared by ALL instances

    def __init__(self, name):
        self.name = name          # unique to each instance

a = Config("first")
b = Config("second")
print(a.version, b.version)       # both 1.0
Config.version = "2.0"
print(a.version, b.version)       # both 2.0 - changed for everyone


# --- __str__ makes printing useful ---
class Thread:
    def __init__(self, title: str, replies: int = 0):
        self.title = title
        self.replies = replies

    def __str__(self) -> str:
        return f"{self.title} ({self.replies} replies)"

    def is_busy(self) -> bool:
        return self.replies > 10


t = Thread("Trading guide", 128)
print(t)                          # Trading guide (128 replies)
print(t.is_busy())                # True

# Without __str__ you would see <__main__.Thread object at 0x...>


# --- Privacy is a convention ---
class Account:
    def __init__(self, balance):
        self.balance = balance         # public
        self._internal_id = 12345      # single _ means "please do not touch"
        self.__secret = "hidden"       # double _ triggers name mangling

acc = Account(100)
print(acc.balance)
print(acc._internal_id)                # accessible - Python trusts you
# print(acc.__secret)                  # AttributeError


# --- Inheritance ---
class Addon:
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version

    def info(self) -> str:
        return f"{self.name} v{self.version}"


class PaidAddon(Addon):
    def __init__(self, name: str, version: str, price: float):
        super().__init__(name, version)      # call the parent constructor
        self.price = price

    def info(self) -> str:                    # override
        return f"{super().info()} - ${self.price}"


free = Addon("ThreadPassword", "1.2")
paid = PaidAddon("Trade", "2.0", 49.99)
print(free.info())
print(paid.info())
print(isinstance(paid, Addon))                # True


# --- Properties: computed values that look like attributes ---
class Post:
    def __init__(self, content: str):
        self.content = content

    @property
    def word_count(self) -> int:
        return len(self.content.split())

    @property
    def preview(self) -> str:
        return self.content[:20] + "..." if len(self.content) > 20 else self.content


p = Post("This is a fairly long forum post about Laravel")
print(p.word_count)               # no parentheses - accessed like an attribute
print(p.preview)


# --- A practical class ---
class ThreadCollection:
    def __init__(self):
        self.threads = []

    def add(self, title: str, replies: int = 0) -> None:
        self.threads.append(Thread(title, replies))

    def busy_threads(self) -> list:
        return [t for t in self.threads if t.is_busy()]

    def total_replies(self) -> int:
        return sum(t.replies for t in self.threads)

    def __len__(self) -> int:
        return len(self.threads)


collection = ThreadCollection()
collection.add("Welcome", 42)
collection.add("Rules", 3)
collection.add("Guide", 128)

print(len(collection))                        # 3 - because of __len__
print(collection.total_replies())             # 173
for t in collection.busy_threads():
    print(t)


# --- Practice ---
# 1. Write an Addon class holding name, version, and a list of features.
# 2. Add a method that returns whether it has a given feature.
# 3. Add __str__ so printing it reads well.
