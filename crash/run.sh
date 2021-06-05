#!/bin/bash
set -ex

for i in {1..8}; do
    ssh node${i} kill -9 `pidof ceph-osd`
    sleep 5
done
