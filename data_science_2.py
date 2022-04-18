import pandas as pd
import random
import numpy as np


# Function การคำนวนทางสถิติ
data = {
    'col 1' : [10, 20, 30],
    'col 2' : [40, 50, 60],
    'col 3' : [70, 80, 90]
}
df = pd.DataFrame(data, index=list('ABC'))
print(df.count()) # นับจำนวนสมาชิกในแต่ล่ะ column
print(df.sum()) # รวมจำนวนในแต่ล่ะ column
print(df.sum(axis=1)) # รวมจำนวนในแต่ล่ะแถว
print(df.sum(axis=0)) # รวมจำนวนในแต่ล่ะ column


