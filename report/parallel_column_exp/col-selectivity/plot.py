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

    with open('pq_16_col_pll.json') as json_file:
        data_dict = json.load(json_file)
        print(data_dict)

    for k, v in reversed(data_dict.items()):
        for val in v:
            results.append([k, val, 'vanilla-parquet-16MB'])

    with open('rpq_16_col_pll.json') as json_file:
        data_dict = json.load(json_file)
        print(data_dict)

    for k, v in reversed(data_dict.items()):
        for val in v:
            results.append([k, val, 'rados-parquet-16MB'])

    # with open('pq_128_col_pll.json') as json_file:
    #     data_dict = json.load(json_file)
    #     print(data_dict)

    # for k, v in reversed(data_dict.items()):
    #     for val in v:
    #         results.append([k, val, 'vanilla-parquet-128MB'])
    

    # with open('rpq_128_col_pll.json') as json_file:
    #     data_dict = json.load(json_file)
    #     print(data_dict)

    # for k, v in reversed(data_dict.items()):
    #     for val in v:
    #         results.append([k, val, 'rados-parquet-128MB'])

    df = pd.DataFrame(np.array(results), columns=['Selectivity (%)', 'Duration (s)', 'Format'])
    df[['Duration (s)']] = df[['Duration (s)']].apply(pd.to_numeric)

    print(df)

    sns_plot = sns.barplot(x="Selectivity (%)", y="Duration (s)", hue='Format', data=df, ci='sd', capsize=.15, errwidth=0.5, palette=palette)
    sns_plot.set(ylim=(0, 80))
    plt.tight_layout()
    plt.savefig(f"plot16_col.pdf", bbox_inches='tight')
