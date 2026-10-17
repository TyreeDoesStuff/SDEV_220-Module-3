# Exercise 12.6
# Create an ordered dictionary and compare it.

from collections import OrderedDict

plain = {"a": 1, "b": 2, "c": 3}

fancy = OrderedDict([
    ("a", 1),
    ("b", 2),
    ("c", 3)
])

print(fancy)
print("Same order:", list(plain) == list(fancy))
