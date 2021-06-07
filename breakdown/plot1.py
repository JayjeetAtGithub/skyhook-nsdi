import os
import sys
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean


if __name__ == "__main__":
    palette1 = sns.color_palette("hls", 8)
    palette2 = sns.color_palette("husl", 8)
    palette3 = sns.color_palette("Set2")

    results = []
    with open('deser.json') as json_file:
        deser_data = json.load(json_file)
    with open('ser.json') as json_file:
        ser_data = json.load(json_file)
    with open('pq.json') as json_file:
        data_dict = json.load(json_file)
    for k, v in data_dict.items():
        results.append([k, mean(v)*1000, 'parquet'])
    with open('rpq.json') as json_file:
        data_dict = json.load(json_file)
    for k, v in data_dict.items():
        results.append([k, mean(v) + mean(ser_data[k]) + mean(deser_data[k]), 'serialization'])
    df = pd.DataFrame(np.array(results), columns=['Selectivity (%)', 'Duration (s)', 'Format'])
    df[['Duration (s)']] = df[['Duration (s)']].apply(pd.to_numeric)
    sns_plot = sns.barplot(x="Selectivity (%)", y="Duration (s)", hue='Format', data=df, ci='sd', capsize=.15, errwidth=0.5, palette=palette1)
    sns_plot.set(ylim=(0, 3000))
    print(df)

    results = []
    with open('pq.json') as json_file:
        data_dict = json.load(json_file)
    for k, v in data_dict.items():
        results.append([k, mean(v)*1000, 'parquet'])
    with open('rpq.json') as json_file:
        data_dict = json.load(json_file)
    for k, v in data_dict.items():
        results.append([k, mean(v) + mean(deser_data[k]), 'deserialization'])
    df = pd.DataFrame(np.array(results), columns=['Selectivity (%)', 'Duration (s)', 'Format'])
    df[['Duration (s)']] = df[['Duration (s)']].apply(pd.to_numeric)
    sns_plot = sns.barplot(x="Selectivity (%)", y="Duration (s)", hue='Format', data=df, ci='sd', capsize=.15, errwidth=0.5, palette=palette2)
    sns_plot.set(ylim=(0, 3000))
    print(df)

    results = []
    with open('pq.json') as json_file:
        data_dict = json.load(json_file)
    for k, v in data_dict.items():
        results.append([k, mean(v)*1000, 'parquet'])
    with open('rpq.json') as json_file:
        data_dict = json.load(json_file)
    for k, v in data_dict.items():
        results.append([k, mean(v), 'rados-parquet'])
    df = pd.DataFrame(np.array(results), columns=['Selectivity (%)', 'Duration (s)', 'Format'])
    df[['Duration (s)']] = df[['Duration (s)']].apply(pd.to_numeric)
    sns_plot = sns.barplot(x="Selectivity (%)", y="Duration (s)", hue='Format', data=df, ci='sd', capsize=.15, errwidth=0.5, palette=palette3)
    sns_plot.set(ylim=(0, 3000))
    print(df)
    plt.legend([],[], frameon=False)
    plt.tight_layout()
    plt.savefig(f"plot.pdf", bbox_inches='tight')

