#!/usr/bin/python3
from add_0 import add  # add_0 appears exactly once

a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))  # ✅ Calls add()
