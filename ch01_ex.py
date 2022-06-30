# https://nomadcoders.co/python-for-beginners/lectures/104

print("test")

####
print("1.0 Data Types of Python (08:48)")
a_str = "like this"
a_number = 3
a_float = 3.12
a_boolean = False
a_none = None

print("type(a_str): ", type(a_str))
print(a_float)
print(a_boolean)
print(a_none)

# python >> snake case
# js >> camel case
print()

####
print("#1.1 Lists in Python (08:30)")
days = ["Mon", "Tue", "Wed", "Thr", "Fri"]
print("Mon" in days)  # return True
print(days[3])
print(days)
days.append("Sat")
print(days)
days.reverse()
print(days)

print()

####
print("#1.2 Tuples and Dicts (06:33)")

print(type(days))

devlunch = {
    "name": "ws",
    "age": 00,
    "korean": True,
    "fav_food": ["bread", "soup"]
}

print(devlunch)
print(devlunch["name"])
devlunch["smart"] = True
print(devlunch)

print()

####
print("#1.3 Built in Functions (04:12)")

age = "18"
print(type(age))
n_age = int(age)
print(n_age)
print(type(n_age))

####
print("#1.4 Creating a Your First Python Function (04:21)")


def say_hello():
    {print("hello")}


print("bye")

####
print("#1.5 Function Arguments (05:45)")


def plus(a, b):
    {print(a + b)}


def minus(a, b):
    {print(a - b)}


plus(2, 5)
minus(2, 5)


def say_hello_two(name="anonymous"):
    {print("hello", name)}

say_hello_two()
say_hello_two("admin")


####
print("#1.6 Returns (05:43)")
def p_plus(a, b):
    print(a + b)


def r_plus(a, b):
    return (a + b)


p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)


####
print("#1.7 Keyworded Arguments (05:52)")
