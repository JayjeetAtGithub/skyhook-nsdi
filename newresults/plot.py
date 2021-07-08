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
                        df_data.append([size, fmt, k, val])

    df = pd.DataFrame(df_data, columns=['size', 'format', 'selectivity', 'time'])
    
    pq_df = df[df['format']=='pq']
    rpq_df = df[df['format']=='rpq']

    print(pq_df)
    print(rpq_df)

    sns.set(style="whitegrid")
    sns.barplot(x="selectivity", y="time", hue="size", ci='sd', capsize=.05, data=pq_df, errwidth=0.5)
    plt.title('vanilla parquet')
    plt.savefig('pq.pdf')

    plt.cla()
    plt.clf()

    sns.barplot(x="selectivity", y="time", hue="size", ci='sd', capsize=.05, data=rpq_df, errwidth=0.5)
    plt.title('rados parquet')
    plt.savefig('rpq.pdf')
    