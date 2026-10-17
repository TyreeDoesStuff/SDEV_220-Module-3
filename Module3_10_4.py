# Exercise 10.4
# Create and catch a custom exception.

class OopsException(Exception):
    pass

try:
    raise OopsException()
except OopsException:
    print("Caught an oops")
