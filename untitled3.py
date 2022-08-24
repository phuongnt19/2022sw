import pandas as pd

import numpy as np

pd.read_csv("data.csv")

df = pd.read_csv("data.csv")

modify_col = ["body__items__item__happenDt", "body__items__item__noticeSdt", "body__items__item__noticeEdt"]

for col in modify_col:
    for i in range(len(df[col])):
        temp = str(df[col][i])
        df[col][i] = f"{temp[:4]}-{temp[4:6]}-{temp[6:]}"

df.to_csv("modified_data.csv", encoding='utf-8')

