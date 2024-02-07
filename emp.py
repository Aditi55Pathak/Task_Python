import pandas as pd
import numpy as np

try:
    count = 0
    with open("emp.txt", "r") as r:
        mylines = r.readlines()
        for lines in mylines:
            print(lines.strip())
            count = count + 1
            print("Total number of lines in file :- ", count)

except Exception as e:
    print(e)
