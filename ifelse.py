import math
import os
import random
import re
import sys

#### if-else practice questions

# question 1
num = int(input())
if num % 2 != 0:
    print("Weird")
elif num % 2 == 0 and num > 20:
    print("Not Weird")
elif num % 2 == 0 and num >= 2 and num <= 5:
    print("Not Weird")
elif num % 2 == 0 and num >= 6 and num <= 20:
    print("Weird")


