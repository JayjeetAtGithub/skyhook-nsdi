import os
import sys
import plotly.express as px
import pandas as pd
import matplotlib as plt

if __name__ == "__main__":
    result = dict()
    with open('client_side.txt') as f:
        lines = f.readlines()

    data = {
        "[1] Stat Fragment": list(),
        "[2] Serialize Scan Request": list(),
        # "exec": list(),
        "[7] Deserialize Result Table": list()
    }

    for line in lines:
        if line.startswith("[1]"):
            parsed = line.split(" ")
            data["[1] Stat Fragment"].append(float(parsed[3]))
        
        if line.startswith("[2]"):
            parsed = line.split(" ")
            data["[2] Serialize Scan Request"].append(float(parsed[5]))

        # if line.startswith("[3]"):
        #     parsed = line.split(" ")
        #     data["exec"].append(float(parsed[2]))

        if line.startswith("[4]"):
            parsed = line.split(" ")
            data["[7] Deserialize Result Table"].append(float(parsed[3]))
    
    for k, v in data.items():
        result[k] = sum(v)/len(v)

    with open('storage_side.txt') as f:
        lines = f.readlines()

    data = {
        "[3] Deserialize Scan Request": list(),
        "[5] Scan Parquet Data": list(),
        "[6] Serialize Result Table": list()
    }

    for line in lines:
        if "[1]" in line:
            parsed = line.split(" ")
            data["[3] Deserialize Scan Request"].append(float(parsed[len(parsed)-2]))

        if "[2]" in line:
            parsed = line.split(" ")
            data["[5] Scan Parquet Data"].append(float(parsed[len(parsed)-2]))

        if "[3]" in line:
            parsed = line.split(" ")
            data["[6] Serialize Result Table"].append(float(parsed[len(parsed)-2]))

    for k, v in data.items():
        result[k] = sum(v)/len(v)

    with open('io.txt') as f:
        lines = f.readlines()

    total_io = 0
    for line in lines:
        parsed = line.split(" ")
        total_io += float(parsed[len(parsed)-2])  
    
    result['[4] Disk I/O'] = total_io

    # breakdown
    total = 0
    for k, v in result.items():
        print(f"{k}: {v}")
        total += v 

    print("total time: ", total)
    result["[5] Scan Parquet Data"] = result["[5] Scan Parquet Data"] - result["[4] Disk I/O"]

    df = pd.DataFrame(result.items())
    print(df)
    fig = px.pie(df, values=1, names=0, color_discrete_sequence=px.colors.sequential.RdBu)
    fig.show()
    fig.write_image("pie.pdf")
