import json as js
import random

with open('data.json') as f:
    data=js.load(f)
    array=data.keys()
    print(array)
    for i in range(0,len(array)):
        print(list(array)[i])