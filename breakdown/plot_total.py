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

    with open('total_pq.json') as json_file:
        data_dict = json.load(json_file)
        print(data_dict)

    for k, v in data_dict.items():
        for val in v:
            results.append([k, val, 'parquet'])

    with open('total_rpq.json') as json_file:
        data_dict = json.load(json_file)
        print(data_dict)

    for k, v in data_dict.items():
        for val in v:
            results.append([k, val, 'rados-parquet'])

    print(results)

    df = pd.DataFrame(np.array(results), columns=['Selectivity (%)', 'Duration (s)', 'Format'])
    df[['Duration (s)']] = df[['Duration (s)']].apply(pd.to_numeric)

    print(df)

    sns_plot = sns.barplot(x="Selectivity (%)", y="Duration (s)", hue='Format', data=df, ci='sd', capsize=.15, errwidth=0.5, palette=palette)
    sns_plot.set(ylim=(0, 4))
    plt.tight_layout()
    plt.savefig(f"plot_total.pdf", bbox_inches='tight')
