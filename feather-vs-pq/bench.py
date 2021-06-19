import pyarrow.feather as feather
import pyarrow.parquet as pq
import time

## parquet
pq_time = list()
for i in range(10):
    s = time.time()
    table = pq.read_table('128MB.parquet')
    e = time.time()
    pq_time.append(e-s)
print(sum(pq_time)/len(pq_time))

## feather
feather_time = list()
for i in range(10):
    s = time.time()
    with open('128MB.feather', 'rb') as f:
        read_df = feather.read_table(f)
    e = time.time()
    feather_time.append(e-s)
print(sum(feather_time)/len(feather_time))

# col reads

## parquet
pq_time = list()
for i in range(10):
    s = time.time()
    table = pq.read_table('128MB.parquet', columns=['total_amount'])
    e = time.time()
    pq_time.append(e-s)
print(sum(pq_time)/len(pq_time))

## feather
feather_time = list()
for i in range(10):
    s = time.time()
    with open('128MB.feather', 'rb') as f:
        read_df = feather.read_table(f, columns=['total_amount'])
    e = time.time()
    feather_time.append(e-s)
print(sum(feather_time)/len(feather_time))
