import os
import sys
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    palette = sns.color_palette('Greys', n_colors=2)
    results = []

    with open('pq_large/result.json') as json_file:
        data_dict = json.load(json_file)
        print(data_dict)

    for k, v in data_dict.items():
        for val in v:
            results.append([k, val, 'parquet-1GB'])

    with open('pq_small/result.json') as json_file:
        data_dict = json.load(json_file)
        print(data_dict)

    for k, v in data_dict.items():
        for val in v:
            results.append([k, val, 'parquet-128MB'])

    with open('rpq/result.json') as json_file:
        data_dict = json.load(json_file)
        print(data_dict)

    for k, v in data_dict.items():
        for val in v:
            results.append([k, val, 'rados-parquet-128MB'])

    print(results)

    df = pd.DataFrame(np.array(results), columns=['Selectivity (%)', 'Duration (s)', 'Format'])
    df[['Duration (s)']] = df[['Duration (s)']].apply(pd.to_numeric)

    print(df)

    sns_plot = sns.barplot(x="Selectivity (%)", y="Duration (s)", hue='Format', data=df, ci='sd', capsize=.15, errwidth=0.5, palette=palette)
    sns_plot.set(ylim=(0, 400))
    plt.tight_layout()
    plt.savefig(f"plot.pdf", bbox_inches='tight')
