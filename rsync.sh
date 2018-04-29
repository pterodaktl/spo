#!/bin/bash

t1=$(date +'%s')
rsync -ah /tmp/file1 testuser@example.com:/tmp
t2=$(date +'%s')
dt12=$(($t2-$t1))

t3=$(date +'%s')
rsync -ah /tmp/file2 testuser@example.com:/tmp
t4=$(date +'%s')
dt34=$(($t4-$t3))

t5=$(date +'%s')
rsync -ah /tmp/file3 testuser@example.com:/tmp
t6=$(date +'%s')
dt56=$(($t6-$t5))

dt=$((($dt12 + $dt34 + $dt56) / 3 ))

echo "$dt"