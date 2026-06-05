# 1) Create a class `India` with three methods:
class India:
    def capital(self):
        return "The capital of India is New Delhi."

    def language(self):
        return "The main language spoken in India is Hindi."

    def type(self):
        return "India is a developing country."

class USA:
    def capital(self):
        return "The capital of USA is Washington, D.C."

    def language(self):
        return "The primary language of USA is English."

    def type(self):
        return "USA is a developed country."

countries = [
    ("India", India()),
    ("United States", USA())
]
                
for name, country in countries:
    print(f"{name}:")
    print(country.capital())
    print(country.language())
    print(country.type())
    print()

# 2) Create another class `USA` with the same method names:

# a) `capital()` to print the capital of USA.

# b) `language()` to print the primary language of USA.

# c) `type()` to print the type of country USA is.

# 3) Create objects for both classes:

# a) `obj_ind = India()`

# b) `obj_usa = USA()`

# 4) Use a common interface (polymorphism) to call the same method names

# on different objects:

# a) Use a `for` loop to iterate through `(obj_ind, obj_usa)`.

# b) For each object `country`, call:

# - `country.capital()`

# - `country.language()`

# - `country.type()`

# (Each object runs its own class implementation of these methods.)