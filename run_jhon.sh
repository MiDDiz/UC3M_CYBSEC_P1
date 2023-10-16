#!/bin/bash

sudo run/john 


sudo run/john --incremental:Alpha --min-length=3 --max-length=7 --format=raw-SHA256-opencl passwd_may_7.csv

sudo run/john --incremental:num --min-len=3 --max-len=7 --format=raw-SHA256-opencl passwd_alphanumsym_4.csv

sudo run/john --incremental:ASCII --min-len=3 --max-len=7 --format=raw-SHA256-opencl passwd_alphanumsym_4.csv

sudo run/john --wordlist=./rockyou.txt --format=raw-SHA256-opencl passwd_rckyou_cased.csv

sudo run/john --wordlist=./rockyou.txt --rules=reverse --format=raw-SHA256-opencl passwd_rckyou_reverse.csv
