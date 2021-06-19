import pyarrow.feather as feather
import pyarrow.parquet as pq
import time
import os

def drop_caches():
    os.system('sync')
    os.system('echo 3 > /proc/sys/vm/drop_caches')
    os.system('sync')

read_time = list()
for i in range(50):
    drop_caches()
    s = time.time()
    open('128MB.feather', 'rb').read()
    e = time.time()
    read_time.append(e-s)
print("read feather blob:", sum(read_time)/len(read_time))


read_time = list()
for i in range(50):
    drop_caches()
    s = time.time()
    open('128MB.parquet', 'rb').read()
    e = time.time()
    read_time.append(e-s)
print("read pq blob:", sum(read_time)/len(read_time))

## parquet
pq_time = list()
for i in range(50):
    drop_caches()
    s = time.time()
    table = pq.read_table('128MB.parquet')
    e = time.time()
    pq_time.append(e-s)
print("parquet all columns:", sum(pq_time)/len(pq_time))

## feather
feather_time = list()
for i in range(50):
    drop_caches()
    s = time.time()
    read_df = feather.read_table('128MB.feather', memory_map=True)
    e = time.time()
    feather_time.append(e-s)
print("feather all columns: ", sum(feather_time)/len(feather_time))

## parquet
pq_time = list()
for i in range(50):
    drop_caches()
    s = time.time()
    table = pq.read_table('128MB.parquet', columns=['total_amount'])
    e = time.time()
    pq_time.append(e-s)
print("parquet single column:", sum(pq_time)/len(pq_time))

## feather
feather_time = list()
for i in range(50):
    drop_caches()
    s = time.time()
    read_df = feather.read_table('128MB.feather', columns=['total_amount'], memory_map=True)
    e = time.time()
    feather_time.append(e-s)
print("feather single column:", sum(feather_time)/len(feather_time))

