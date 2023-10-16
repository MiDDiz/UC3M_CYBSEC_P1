#!/bin/zsh

# minusculas y mayusculas
for type in min may 
do
    for i in 3 4 5 6 7
    do
        echo "---- PROCESSING passwd_${type}_${i}.csv ----"
        : > run/john.log
        sudo run/john --incremental:Alpha --min-length=3 --max-length=7 --format=raw-SHA256-opencl passwd_${type}_${i}.csv
        cat run/john.log | grep Cracked | python3 run_stats.py > stats_${type}_${i}.out
    done
done

# numeros 
for i in 3 4 5 6 7
do
    echo "---- PROCESSING passwd_num_${i}.csv ----"
    : > run/john.log
    sudo run/john --incremental:num --min-length=3 --max-length=7 --format=raw-SHA256-opencl passwd_num_${i}.csv
    cat run/john.log | grep Cracked | python3 run_stats.py > stats_num_${i}.out
done

# alphanumsym 
for i in 3 4 5 6 7
do
    echo "---- PROCESSING passwd_alphanumsym_${i}.csv ----"
    : > run/john.log
    sudo run/john --incremental:ASCII --min-length=3 --max-length=7 --format=raw-SHA256-opencl passwd_alphanumsym_${i}.csv
    cat run/john.log | grep Cracked | python3 run_stats.py > stats_alphanumsym_${i}.out
done

echo "---- PROCESSING passwd_rckyou_cased.csv ----"
: > run/john.log
sudo run/john --wordlist=./rockyou.txt --format=raw-SHA256-opencl passwd_rckyou_cased.csv
cat run/john.log | grep Cracked | python3 run_stats.py > passwd_rckyou_cased.out

echo "---- PROCESSING passwd_rckyou_reverse.csv ----"
: > run/john.log
sudo run/john --wordlist=./rockyou.txt --rules=reverse --format=raw-SHA256-opencl passwd_rckyou_reverse.csv
cat run/john.log | grep Cracked | python3 run_stats.py > passwd_rckyou_reverse.out

echo "---- PROCESSING passwd_rckyou_cased.csv ----"
: > run/john.log
sudo run/john --wordlist=./rockyou.txt --format=raw-SHA256-opencl passwd_rckyou_cased.csv
cat run/john.log | grep Cracked | python3 run_stats.py > passwd_rckyou_cased.out

echo "---- PROCESSING passwd_rckyou_cased.csv ----"
: > run/john.log
sudo run/john --wordlist=./rockyou.txt --format=raw-SHA256-opencl passwd_rckyou_cased.csv
cat run/john.log | grep Cracked | python3 run_stats.py > passwd_rckyou_cased.out

echo "---- PROCESSING passwd_rckyou_cased.csv ----"
: > run/john.log
sudo run/john --wordlist=./rockyou.txt --format=raw-SHA256-opencl passwd_rckyou_cased.csv
cat run/john.log | grep Cracked | python3 run_stats.py > passwd_rckyou_cased.out

#
#sudo run/john --wordlist=./rockyou.txt --format=raw-SHA256-opencl passwd_rckyou_cased.csv
#
#sudo run/john --wordlist=./rockyou.txt --rules=reverse --format=raw-SHA256-opencl passwd_rckyou_reverse.csv
