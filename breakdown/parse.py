import os
data = []
if __name__ == "__main__":
    with open('output', 'r') as f:
        lines = f.readlines()

    for line in lines:
        if "<cls>" in line:
            line = line.rstrip()
            line = int(line.split(" ")[7])
            data.append(line)

print(data)
