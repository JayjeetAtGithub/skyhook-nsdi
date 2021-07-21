import os
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sizes = [4,8,16,32,64,128]
    formats = ['pq', 'rpq']

    df_data = []

    for fmt in formats:
        for size in sizes:
            name = f"{fmt}_{size}MB.uc.json"
            with open(name) as f:
                data = json.loads(f.read())
                for k, v in data.items():
                    for val in v:
                        df_data.append([f"{fmt}/{size}MB", k, val])

    df = pd.DataFrame(df_data, columns=['config', 'selectivity', 'time'])
    sns.set(style="whitegrid")
    sns.set(rc={'figure.figsize':(20.7,8.27)})

    sns.barplot(x="selectivity", y="time", hue="config", ci='sd', capsize=.05, data=df, errwidth=0.5)
    plt.title('vanilla parquet vs rados parquet over file sizes')
    plt.savefig('cumulative.pdf')
    plt.cla()
    plt.clf()
