import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

if __name__ == "__main__":
    df = pd.read_csv('network_traffic_pq.csv')
    data_dict = df.to_dict()

    time = list(data_dict['Time'])

    values = list()
    for k, v in data_dict['Values'].items():
        values.append(int(v))

    plot_dict = {
        'time': time,
        'throughput': values,
        'Type': 'vanilla-parquet'
    }

    df1 = pd.DataFrame(plot_dict)

    df = pd.read_csv('network_traffic_rpq.csv')
    data_dict = df.to_dict()

    time = list(data_dict['Time'])

    values = list()
    for k, v in data_dict['Values'].items():
        values.append(int(v))

    plot_dict = {
        'time': time,
        'throughput': values,
        'Type': 'rados-parquet'
    }

    df2 = pd.DataFrame(plot_dict)

    final_df = df1.append(df2)

    sns.lineplot(
        x="time", 
        y="throughput", 
        hue="Type", 
        data=final_df, 
        style="Type", 
        markers=True, 
        dashes=False, 
        palette="mako_r"
    )

    plt.title('Network Traffic')
    plt.xlabel('Experiment Duration (s)')
    plt.ylabel('Network Throughput (MB/s)')
    plt.tight_layout()
    plt.savefig('plot.pdf')
