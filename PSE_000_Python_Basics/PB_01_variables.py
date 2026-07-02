# Python Basics - Variables
# -----------------------------------------------------------------------------
# Variables are containers for storing data values. In Python, you don't need
# to declare a variable's type explicitly — it is inferred at assignment.
#
# Key concepts:
# 1. Dynamic typing: type is determined at runtime.
# 2. Naming: snake_case by convention, must start with letter or underscore.
# 3. Multiple assignment: assign multiple variables in one line.
# 4. Unpacking: extract values from sequences into variables.
# 5. Constants: use UPPER_CASE (convention only, not enforced).
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Variable Assignment
# =============================================================================


name = "Alice"          # str
age = 30                # int
height = 5.7            # float
is_student = True       # bool

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")


# =============================================================================
# Dynamic Typing
# =============================================================================


x = 10          # x is an int
print(f"x = {x}, type: {type(x).__name__}")

x = "hello"    # now x is a str
print(f"x = {x}, type: {type(x).__name__}")

x = [1, 2, 3]  # now x is a list
print(f"x = {x}, type: {type(x).__name__}")


# =============================================================================
# Multiple Assignment
# =============================================================================


# Same value to multiple variables
a = b = c = 0
print(f"a={a}, b={b}, c={c}")

# Different values in one line
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")


# =============================================================================
# Unpacking
# =============================================================================


# Unpack a list
coordinates = [10, 20, 30]
lat, lon, alt = coordinates
print(f"Lat: {lat}, Lon: {lon}, Alt: {alt}")

# Unpack with * (collect remaining items)
first, *rest = [1, 2, 3, 4, 5]
print(f"First: {first}, Rest: {rest}")

# Swap variables (Pythonic)
m, n = 5, 10
m, n = n, m
print(f"After swap: m={m}, n={n}")


# =============================================================================
# Variable Scope (Local vs Global)
# =============================================================================


global_var = "I am global"


def demo_scope():
    local_var = "I am local"
    print(f"Inside function: {global_var}")
    print(f"Inside function: {local_var}")


demo_scope()
print(f"Outside function: {global_var}")
# print(local_var)  # This would raise NameError


# =============================================================================
# Constants (Convention)
# =============================================================================


MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"

print(f"Max retries: {MAX_RETRIES}, Timeout: {DEFAULT_TIMEOUT}s")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Variable Assignment ===")
    language = "Python"
    version = 3.12
    print(f"Language: {language}, Version: {version}")

    print("\n=== Dynamic Typing ===")
    var = 42
    print(f"var = {var} ({type(var).__name__})")
    var = "now a string"
    print(f"var = {var} ({type(var).__name__})")

    print("\n=== Multiple Assignment ===")
    red, green, blue = 255, 128, 0
    print(f"RGB: ({red}, {green}, {blue})")

    print("\n=== Unpacking ===")
    person = ("Bob", 25, "Engineer")
    name, age, role = person
    print(f"{name}, {age}, {role}")

    print("\n=== Swapping ===")
    x, y = 1, 2
    print(f"Before: x={x}, y={y}")
    x, y = y, x
    print(f"After:  x={x}, y={y}")


if __name__ == "__main__":
    main()
