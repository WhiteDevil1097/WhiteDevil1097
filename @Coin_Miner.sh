#!/bin/bash

# Update package list and install dependencies
sudo apt-get update
sudo apt-get install -y build-essential automake autoconf libcurl4-openssl-dev git

# Clone cpuminer source code
git clone https://github.com/pooler/cpuminer.git
cd cpuminer

# Build cpuminer
./autogen.sh
./configure CFLAGS="-O3"
make

# Start mining (replace with the pool and wallet address of your choice)
./minerd -o stratum+tcp://litecoinpool.org:3333 -u whitedevil1096 -p Whitedevil1096
# Note:
# - Replace `your_username.worker_name` and `your_password` with your actual credentials for the mining pool.
# - Replace the pool URL with the one you want to use.

echo "Mining started. Press Ctrl+C to stop."
i
